from fastapi import APIRouter
from backend.database import db

router = APIRouter()


@router.get("/crime-trends")
def crime_trends():

    pipeline = [
        {
            "$group": {
                "_id": "$Date",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "_id": 1
            }
        }
    ]

    return list(db["cases"].aggregate(pipeline))