📖 Overview

The Karnataka Crime Intelligence Platform is an AI-driven crime analytics system designed to assist law enforcement agencies in making faster and smarter decisions. It combines crime data visualization, predictive analytics, and interactive dashboards to provide actionable insights from large-scale crime records.

The platform centralizes crime information, identifies hotspots, predicts crime priorities using Machine Learning, and presents intelligence through an intuitive dashboard.

🎯 Problem Statement

Crime data is often scattered across multiple systems, making it difficult for law enforcement agencies to:

Identify crime trends
Detect crime hotspots
Prioritize investigations
Allocate police resources efficiently
Generate real-time intelligence

Manual analysis is slow and limits proactive policing.

Our platform addresses these challenges through centralized analytics and AI-powered decision support.

✨ Features
📊 Crime Analytics Dashboard
Overall crime statistics
Total registered cases
Priority distribution
Crime category distribution
Investigation status overview
Interactive visualizations
🗺️ Crime Hotspot Map
Interactive Karnataka crime map
GPS-based crime visualization
Filter by
District
Crime Type
Priority
Case information popups
🤖 AI Crime Priority Prediction

Predicts the priority level of newly reported crimes using Machine Learning.

Input Features
Crime Type
District
Police Station
Weapon Used
Vehicle Used
Output
Predicted Priority
Model Confidence
🔍 Crime Intelligence Explorer

Search and explore:

FIR details
Crime category
Police station
Investigation status
Assigned officer
Historical records
📈 Crime Analytics

Visualizations include:

Crime distribution
Priority distribution
Status distribution
District-wise analysis
Operational insights
⚠ Risk Intelligence

Provides:

Risk scoring
Investigation insights
Crime severity indicators
🏗 System Architecture
                    Crime Records
                          │
                          ▼
                    MongoDB Database
                          │
                          ▼
                  FastAPI REST Backend
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
     Dashboard       Crime Map      AI Prediction
          │
          ▼
      Streamlit Frontend
🛠 Technology Stack
Frontend
Streamlit
Plotly
Backend
FastAPI
Python
Database
MongoDB
Machine Learning
Scikit-learn
Joblib
Data Processing
Pandas
NumPy
📂 Project Structure
Datathon/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── database.py
│   └── main.py
│
├── dashboard/
│   ├── Home.py
│   └── pages/
│       ├── Dashboard.py
│       ├── Crime_Map.py
│       ├── AI_Prediction.py
│       ├── Intelligence.py
│       └── Analytics.py
│
├── ml/
│   ├── training.py
│   ├── label_encoders.pkl
│   └── model.pkl
│
├── data/
│
├── requirements.txt
└── README.md
