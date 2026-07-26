from typing import Optional

from backend.database import db


def get_all_cases(
    limit: int = 100,
    skip: int = 0,
    district: Optional[str] = None,
    priority: Optional[str] = None,
    status: Optional[str] = None,
    crime: Optional[str] = None,
):
    """
    Fetch cases with optional filters and pagination.
    """

    query = {}

    if district:
        query["DistrictName"] = district

    if priority:
        query["Priority"] = priority

    if status:
        query["Status"] = status

    if crime:
        query["CrimeHeadName"] = crime

    cursor = (
        db["cases"]
        .find(query, {"_id": 0})
        .sort("Date", -1)
        .skip(skip)
        .limit(limit)
    )

    return list(cursor)


def get_case(case_id: int):
    """
    Fetch one case.
    """

    return db["cases"].find_one(
        {
            "CaseID": case_id
        },
        {
            "_id": 0
        }
    )


def search_cases(keyword: str):
    """
    Search across multiple text fields.
    """

    regex = {
        "$regex": keyword,
        "$options": "i"
    }

    query = {
        "$or": [
            {"FIRNumber": regex},
            {"CrimeHeadName": regex},
            {"DistrictName": regex},
            {"StationName": regex},
            {"Priority": regex},
            {"Status": regex},
        ]
    }

    return list(
        db["cases"].find(
            query,
            {"_id": 0}
        )
    )


def get_case_statistics():
    """
    Dashboard statistics.
    """

    total = db["cases"].count_documents({})

    pending = db["cases"].count_documents(
        {
            "Status": "Pending"
        }
    )

    closed = db["cases"].count_documents(
        {
            "Status": "Closed"
        }
    )

    high_priority = db["cases"].count_documents(
        {
            "Priority": "High"
        }
    )

    return {
        "TotalCases": total,
        "PendingCases": pending,
        "ClosedCases": closed,
        "HighPriorityCases": high_priority,
    }


def get_cases_by_officer(officer_id: int):

    return list(
        db["cases"].find(
            {
                "OfficerID": officer_id
            },
            {
                "_id": 0
            }
        )
    )


def get_cases_by_station(station_id: int):

    return list(
        db["cases"].find(
            {
                "StationID": station_id
            },
            {
                "_id": 0
            }
        )
    )