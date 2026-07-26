from fastapi import APIRouter
from backend.database import db

router = APIRouter()

@router.get("/districts")
def get_districts():
    districts = list(db["districts"].find({}, {"_id": 0}))
    return districts