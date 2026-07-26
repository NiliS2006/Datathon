import os
import random
import pandas as pd
from datetime import timedelta


def generate_arrests():

    history = pd.read_csv("../data/generated/criminal_history.csv")
    cases = pd.read_csv("../data/generated/case_master.csv")

    case_dates = dict(zip(cases["CaseID"], pd.to_datetime(cases["Date"])))

    rows = []

    arrest_id = 1

    for _, criminal in history.iterrows():

        if criminal["ArrestStatus"] != "Arrested":
            continue

        case_date = case_dates.get(criminal["CaseID"])

        arrest_date = case_date + timedelta(
            days=random.randint(0, 30)
        )

        rows.append({

            "ArrestID": arrest_id,

            "PersonID": criminal["PersonID"],

            "CaseID": criminal["CaseID"],

            "ArrestDate": arrest_date,

            "CustodyDays": random.randint(1, 90),

            "BailGranted": random.choice([True, False])

        })

        arrest_id += 1

    df = pd.DataFrame(rows)

    output = "../data/generated"

    os.makedirs(output, exist_ok=True)

    df.to_csv(
        os.path.join(output, "arrests.csv"),
        index=False
    )

    print(df.head())

    print(f"\nGenerated {len(df)} Arrest Records")


if __name__ == "__main__":

    generate_arrests()