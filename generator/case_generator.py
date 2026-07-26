import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

crime_types = [
    "Theft",
    "Robbery",
    "Murder",
    "Assault",
    "Cyber Crime",
    "Drug Trafficking",
    "Kidnapping",
    "Domestic Violence",
    "Fraud",
    "Burglary"
]

crime_category = {
    "Theft":"Property Crime",
    "Robbery":"Property Crime",
    "Burglary":"Property Crime",
    "Murder":"Violent Crime",
    "Assault":"Violent Crime",
    "Kidnapping":"Violent Crime",
    "Cyber Crime":"Cyber Crime",
    "Fraud":"Financial Crime",
    "Drug Trafficking":"Organized Crime",
    "Domestic Violence":"Social Crime"
}

districts = pd.read_csv("data/generated/districts.csv")

records = []

for i in range(10000):

    district = districts.sample(1).iloc[0]

    lat = district["Latitude"] + random.uniform(-0.08,0.08)
    lon = district["Longitude"] + random.uniform(-0.08,0.08)

    crime = random.choice(crime_types)

    records.append({

        "CaseID":i+1,

        "FIRNumber":f"FIR-{100000+i}",

        "CrimeType":crime,

        "CrimeCategory":crime_category[crime],

        "District":district["DistrictName"],

        "PoliceStation":fake.city()+" PS",

        "Latitude":lat,

        "Longitude":lon,

        "Date":fake.date_between(
            start_date="-2y",
            end_date="today"
        ),

        "Time":fake.time(),

        "Severity":random.choice(
            ["Low","Medium","High"]
        ),

        "Status":random.choice(
            [
                "Open",
                "Under Investigation",
                "Chargesheet Filed",
                "Closed"
            ]
        ),

        "VictimID":random.randint(1,25000),

        "SuspectID":random.randint(1,8000),

        "Weapon":random.choice(
            [
                "Knife",
                "Gun",
                "Blunt Object",
                "None",
                "Unknown"
            ]
        ),

        "RepeatOffender":random.choice(
            [True,False]
        ),

        "GangID":random.randint(1,250),

        "EstimatedLoss":random.randint(
            1000,
            500000
        )

    })

df = pd.DataFrame(records)

df.to_csv(
    "data/generated/cases.csv",
    index=False
)

print(df.head())