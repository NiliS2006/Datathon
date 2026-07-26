from backend.database import db


def crime_by_type():

    pipeline = [

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

    ]

    return list(
        db["cases"].aggregate(pipeline)
    )


def crime_by_district():

    pipeline = [

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

    ]

    return list(
        db["cases"].aggregate(pipeline)
    )