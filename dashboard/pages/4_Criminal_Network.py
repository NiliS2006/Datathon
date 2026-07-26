import streamlit as st
import requests
import networkx as nx
import plotly.graph_objects as go

st.set_page_config(
    page_title="Criminal Network",
    page_icon="🕸️",
    layout="wide"
)

st.title("🕸️ Criminal Intelligence Network")

API = "http://127.0.0.1:8000/intelligence/cases"

try:

    response = requests.get(API)

    if response.status_code != 200:
        st.error("Backend is not responding.")
        st.stop()

    data = response.json()

except Exception:
    st.error("Cannot connect to FastAPI Backend.")
    st.stop()

if len(data) == 0:
    st.warning("No intelligence data available.")
    st.stop()

# ---------------------------------------
# Sidebar
# ---------------------------------------

crime_list = sorted(list(set(i["Crime"] for i in data)))

crime_filter = st.sidebar.selectbox(
    "Crime Type",
    ["All"] + crime_list
)

if crime_filter != "All":
    data = [i for i in data if i["Crime"] == crime_filter]

# ---------------------------------------
# Build Network
# ---------------------------------------

G = nx.Graph()

for row in data:

    case = f"Case {row['CaseID']}"

    officer = row["Officer"]

    station = row["PoliceStation"]

    crime = row["Crime"]

    district = row["District"]

    G.add_node(
        case,
        group="Case"
    )

    G.add_node(
        officer,
        group="Officer"
    )

    G.add_node(
        station,
        group="Station"
    )

    G.add_node(
        crime,
        group="Crime"
    )

    G.add_node(
        district,
        group="District"
    )

    G.add_edge(case, officer)
    G.add_edge(case, station)
    G.add_edge(case, crime)
    G.add_edge(case, district)

# ---------------------------------------
# KPIs
# ---------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Cases", len([n for n,d in G.nodes(data=True) if d["group"]=="Case"]))

c2.metric("Officers", len([n for n,d in G.nodes(data=True) if d["group"]=="Officer"]))

c3.metric("Stations", len([n for n,d in G.nodes(data=True) if d["group"]=="Station"]))

c4.metric("Connections", G.number_of_edges())

st.divider()

# ---------------------------------------
# Network Layout
# ---------------------------------------

pos = nx.spring_layout(
    G,
    seed=42,
    k=0.45
)

edge_x = []
edge_y = []

for edge in G.edges():

    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]

    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    mode="lines",
    hoverinfo="none",
    line=dict(width=1, color="#999")
)

colors = {
    "Case":"red",
    "Officer":"blue",
    "Station":"green",
    "Crime":"purple",
    "District":"orange"
}

node_x = []
node_y = []
node_text = []
node_color = []

for node in G.nodes():

    x,y = pos[node]

    node_x.append(x)
    node_y.append(y)

    node_text.append(node)

    node_color.append(
        colors[G.nodes[node]["group"]]
    )

node_trace = go.Scatter(

    x=node_x,

    y=node_y,

    mode="markers+text",

    text=node_text,

    textposition="top center",

    hoverinfo="text",

    marker=dict(
        size=14,
        color=node_color,
        line=dict(width=2,color="black")
    )
)

fig = go.Figure(
    data=[edge_trace,node_trace]
)

fig.update_layout(

    title="Criminal Intelligence Relationship Graph",

    showlegend=False,

    height=800,

    margin=dict(
        l=20,
        r=20,
        t=60,
        b=20
    ),

    xaxis=dict(showgrid=False,zeroline=False,visible=False),

    yaxis=dict(showgrid=False,zeroline=False,visible=False)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("Connected Intelligence Records")

st.dataframe(
    data,
    use_container_width=True,
    hide_index=True
)