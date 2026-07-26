from fastapi import APIRouter
from backend.database import db

router = APIRouter()


@router.get("/crime-locations")
def crime_locations():

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

        {
            "$unwind": {
                "path": "$crime",
                "preserveNullAndEmptyArrays": True
            }
        },

        {
            "$unwind": {
                "path": "$station",
                "preserveNullAndEmptyArrays": True
            }
        },

        {
            "$unwind": {
                "path": "$officer",
                "preserveNullAndEmptyArrays": True
            }
        },

        {
            "$project": {

                "_id": 0,

                "CaseID": 1,
                "Date": 1,
                "Latitude": 1,
                "Longitude": 1,
                "Priority": 1,
                "Status": 1,

                "Crime": "$crime.CrimeHeadName",
                "District": "$station.DistrictName",
                "PoliceStation": "$station.StationName",
                "Officer": "$officer.EmployeeName"
            }
        }

    ]

    return list(db["cases"].aggregate(pipeline))