from backend.database import db


def get_employee_lookup():

    employees = {}

    cursor = db["employees"].find(
        {},
        {
            "_id": 0,
            "EmployeeID": 1,
            "OfficerName": 1,
            "Rank": 1,
            "StationName": 1,
            "DistrictName": 1
        }
    )

    for emp in cursor:

        employees[emp["EmployeeID"]] = emp

    return employees