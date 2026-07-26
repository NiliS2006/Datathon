from fastapi import APIRouter, HTTPException
from backend.database import db

router = APIRouter(tags=["Assignment"])


@router.post("/assignment/recommend")
def recommend_officer(
    district: str,
    priority: str
):
    """
    Recommend the least busy officer in a district.
    """

    try:

        station = db["police_stations"].find_one(
            {
                "DistrictName": district
            }
        )

        if not station:
            raise HTTPException(
                status_code=404,
                detail="District not found"
            )

        station_id = station["StationID"]

        officers = list(

            db["employees"].find(
                {
                    "StationID": station_id
                },
                {
                    "_id": 0
                }
            )

        )

        if not officers:
            raise HTTPException(
                status_code=404,
                detail="No officers available"
            )

        best = None
        minimum = float("inf")

        for officer in officers:

            workload = db["cases"].count_documents(

                {

                    "OfficerID": officer["EmployeeID"],

                    "Status": {
                        "$ne": "Closed"
                    }

                }

            )

            if workload < minimum:

                minimum = workload

                best = officer

        return {

            "RecommendedOfficer": best["OfficerName"],

            "OfficerID": best["EmployeeID"],

            "StationID": station_id,

            "CurrentWorkload": minimum,

            "SuggestedPriority": priority

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )