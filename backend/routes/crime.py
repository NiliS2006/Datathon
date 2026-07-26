from fastapi import APIRouter
from backend.database import db

router = APIRouter()

@router.get("/crime-heads")
def crime_heads():

    heads = list(
        db["crime_heads"].find({}, {"_id":0})
    )

    return heads