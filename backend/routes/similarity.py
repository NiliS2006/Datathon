from fastapi import APIRouter
from backend.database import db

router = APIRouter(tags=["Similarity"])


@router.get("/cases/{case_id}/similar")
def similar(case_id: int):

    current = db["cases"].find_one(
        {
            "CaseID": case_id
        }
    )

    if not current:
        return []

    query = {

        "CrimeHeadID": current["CrimeHeadID"],

        "StationID": current["StationID"],

        "CaseID": {
            "$ne": case_id
        }

    }

    cursor = db["cases"].find(
        query,
        {
            "_id":0
        }
    ).limit(5)

    return list(cursor)