from backend.database import db


def get_all_crime_heads():
    return list(
        db["crime_heads"].find(
            {},
            {"_id": 0}
        )
    )


def get_crime_head_lookup():
    crimes = {}

    cursor = db["crime_heads"].find(
        {},
        {
            "_id": 0,
            "CrimeHeadID": 1,
            "CrimeHeadName": 1
        }
    )

    for crime in cursor:
        crimes[crime["CrimeHeadID"]] = crime["CrimeHeadName"]

    return crimes