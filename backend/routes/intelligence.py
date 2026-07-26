from fastapi import APIRouter
from backend.database import db

router = APIRouter()


@router.get("/intelligence/cases")
def get_cases():

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
            "$lookup": {
                "from": "crime_subheads",
                "localField": "CrimeSubHeadID",
                "foreignField": "CrimeSubHeadID",
                "as": "subcrime"
            }
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
            "$lookup": {
                "from": "employees",
                "localField": "OfficerID",
                "foreignField": "EmployeeID",
                "as": "officer"
            }
        },

        {"$unwind": "$crime"},
        {"$unwind": "$subcrime"},
        {"$unwind": "$station"},
        {"$unwind": "$officer"},

        {
            "$project": {
                "_id": 0,
                "CaseID": 1,
                "FIRNumber": 1,
                "Crime": "$crime.CrimeHeadName",
                "SubCrime": "$subcrime.CrimeSubHeadName",
                "District": "$station.DistrictName",
                "PoliceStation": "$station.StationName",
                "Officer": "$officer.OfficerName",
                "Priority": 1,
                "Status": 1,
                "Date": 1,
                "Latitude": 1,
                "Longitude": 1
            }
        },

        {
            "$sort": {
                "Date": -1
            }
        }

    ]

    return list(db["cases"].aggregate(pipeline))