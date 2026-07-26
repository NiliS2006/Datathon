from fastapi import APIRouter
from backend.database import db

router = APIRouter(tags=["Officer Analytics"])


@router.get("/analytics/officers")
def officer_performance():

    pipeline = [

        {
            "$lookup": {

                "from": "employees",

                "localField": "OfficerID",

                "foreignField": "EmployeeID",

                "as": "Officer"

            }

        },

        {

            "$unwind": "$Officer"

        },

        {

            "$group": {

                "_id": "$Officer.OfficerName",

                "CasesAssigned": {
                    "$sum": 1
                },

                "Pending": {

                    "$sum": {

                        "$cond": [

                            {

                                "$eq": [
                                    "$Status",
                                    "Pending"
                                ]

                            },

                            1,

                            0

                        ]

                    }

                },

                "Closed": {

                    "$sum": {

                        "$cond": [

                            {

                                "$eq": [
                                    "$Status",
                                    "Closed"
                                ]

                            },

                            1,

                            0

                        ]

                    }

                }

            }

        },

        {

            "$sort": {

                "CasesAssigned": -1

            }

        }

    ]

    return list(
        db["cases"].aggregate(pipeline)
    )