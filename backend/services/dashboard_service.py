from backend.database import db


def get_dashboard_data():
    cases = db["cases"]

    # ----------------------------
    # Summary
    # ----------------------------

    total_cases = cases.count_documents({})

    open_cases = cases.count_documents({
        "Status": "Under Investigation"
    })

    solved_cases = cases.count_documents({
        "Status": {
            "$in": [
                "Closed",
                "Charge Sheet Filed"
            ]
        }
    })

    repeat_offenders = db["criminal_history"].count_documents(
        {
            "NumberOfPreviousCases": {
                "$gte": 2
            }
        }
    )

    # ----------------------------
    # Crime Distribution
    # ----------------------------

    crime_types = list(
        cases.aggregate([
            {
                "$lookup": {
                    "from": "crime_heads",
                    "localField": "CrimeHeadID",
                    "foreignField": "CrimeHeadID",
                    "as": "crime"
                }
            },
            {
                "$unwind": "$crime"
            },
            {
                "$group": {
                    "_id": "$crime.CrimeHeadName",
                    "count": {
                        "$sum": 1
                    }
                }
            },
            {
                "$sort": {
                    "count": -1
                }
            }
        ])
    )

    # ----------------------------
    # Priority Distribution
    # ----------------------------

    priority = list(
        cases.aggregate([
            {
                "$group": {
                    "_id": "$Priority",
                    "count": {
                        "$sum": 1
                    }
                }
            },
            {
                "$sort": {
                    "count": -1
                }
            }
        ])
    )

    # ----------------------------
    # District Distribution
    # ----------------------------

    districts = list(
        cases.aggregate([
            {
                "$lookup": {
                    "from": "police_stations",
                    "localField": "StationID",
                    "foreignField": "StationID",
                    "as": "station"
                }
            },
            {
                "$unwind": "$station"
            },
            {
                "$group": {
                    "_id": "$station.DistrictName",
                    "count": {
                        "$sum": 1
                    }
                }
            },
            {
                "$sort": {
                    "count": -1
                }
            }
        ])
    )

    # ----------------------------
    # Recent Cases
    # ----------------------------

    recent_cases = list(
        cases.aggregate([
            {
                "$lookup": {
                    "from": "crime_heads",
                    "localField": "CrimeHeadID",
                    "foreignField": "CrimeHeadID",
                    "as": "crime"
                }
            },
            {
                "$unwind": "$crime"
            },
            {
                "$lookup": {
                    "from": "police_stations",
                    "localField": "StationID",
                    "foreignField": "StationID",
                    "as": "station"
                }
            },
            {
                "$unwind": "$station"
            },
            {
                "$project": {
                    "_id": 0,
                    "CaseID": 1,
                    "Crime": "$crime.CrimeHeadName",
                    "District": "$station.DistrictName",
                    "Priority": 1,
                    "Status": 1,
                    "Date": 1
                }
            },
            {
                "$sort": {
                    "Date": -1
                }
            },
            {
                "$limit": 15
            }
        ])
    )

    return {
        "summary": {
            "total_cases": total_cases,
            "open_cases": open_cases,
            "solved_cases": solved_cases,
            "repeat_offenders": repeat_offenders
        },
        "crime_types": crime_types,
        "priority": priority,
        "districts": districts,
        "recent_cases": recent_cases
    }