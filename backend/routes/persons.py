from fastapi import APIRouter
from backend.database import db

router = APIRouter()

@router.get("/persons")
def get_persons(limit: int = 100):

    persons = list(
        db["persons"].find({}, {"_id":0}).limit(limit)
    )

    return persons