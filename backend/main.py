from fastapi import FastAPI

print("========== MAIN.PY LOADED ==========")

from backend.routes.cases import router as cases_router
print("Cases loaded")

from backend.routes.map import router as map_router
print("Map loaded")

from backend.routes.predict import router as predict_router
print("Predict loaded")

from backend.routes.intelligence import router as intelligence_router
print("Intelligence loaded")

from backend.routes.analytics import router as analytics_router
print("Analytics loaded")

from backend.routes.risk import router as risk_router
print("Risk loaded")

from backend.routes.dashboard import router as dashboard_router
print("Dashboard loaded")

app = FastAPI(
    title="Crime Intelligence Platform",
    version="1.0.0"
)

app.include_router(cases_router)
app.include_router(map_router)
app.include_router(predict_router)
app.include_router(intelligence_router)
app.include_router(analytics_router)
app.include_router(risk_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"message": "API Running"}

    print("\n========== REGISTERED ROUTES ==========")
for route in app.routes:
    print(route.path)
print("=======================================\n")