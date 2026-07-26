import pandas as pd

from pymongo import MongoClient

client = MongoClient()

db = client.crime_intelligence_db

df = pd.read_csv("data/generated/cases.csv")

db.cases.insert_many(
    df.to_dict("records")
)

print("Imported",len(df))