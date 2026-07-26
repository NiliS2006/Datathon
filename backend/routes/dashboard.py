from fastapi import APIRouter
from backend.services.dashboard_service import get_dashboard_data

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return get_dashboard_data()