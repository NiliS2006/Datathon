from pymongo import MongoClient

try:

    client = MongoClient("mongodb://localhost:27017/")

    db = client["crime_intelligence"]

    print("Connected Successfully!")

    print("Database Name:", db.name)

except Exception as e:

    print(e)