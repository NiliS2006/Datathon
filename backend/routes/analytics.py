from fastapi import APIRouter
from backend.database import db

router = APIRouter(tags=["Analytics"])


@router.get("/analytics/overview")
def overview():

    total = db["cases"].count_documents({})

    open_cases = db["cases"].count_documents(
        {"Status": "Pending"}
    )

    closed = db["cases"].count_documents(
        {"Status": "Closed"}
    )

    high = db["cases"].count_documents(
        {"Priority": "High"}
    )

    return {
        "TotalCases": total,
        "PendingCases": open_cases,
        "ClosedCases": closed,
        "HighPriority": high,
        "ResolutionRate": round(
            (closed / total) * 100,
            2
        ) if total else 0
    }


@router.get("/analytics/crime-distribution")
def crime_distribution():

    pipeline = [

        {
            "$group": {
                "_id": "$CrimeHeadName",
                "Cases": {
                    "$sum": 1
                }
            }
        },

        {
            "$sort": {
                "Cases": -1
            }
        }

    ]

    return list(
        db["cases"].aggregate(pipeline)
    )


@router.get("/analytics/priority-distribution")
def priority_distribution():

    pipeline = [

        {
            "$group": {

                "_id": "$Priority",

                "Cases": {
                    "$sum": 1
                }

            }

        }

    ]

    return list(
        db["cases"].aggregate(pipeline)
    )


@router.get("/analytics/status-distribution")
def status_distribution():

    pipeline = [

        {

            "$group": {

                "_id": "$Status",

                "Cases": {
                    "$sum": 1
                }

            }

        }

    ]

    return list(
        db["cases"].aggregate(pipeline)
    )