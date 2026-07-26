import os
import random
import pandas as pd

from master_data import COURTS


def generate_court_cases():

    cases = pd.read_csv("../data/generated/case_master.csv")

    rows = []

    court_id = 1

    for _, case in cases.iterrows():

        rows.append({

            "CourtCaseID": court_id,

            "CaseID": case["CaseID"],

            "CourtName": random.choice(COURTS),

            "JudgeName": f"Justice {random.randint(1,500)}",

            "HearingCount": random.randint(1,20),

            "Judgement": random.choice([
                "Pending",
                "Convicted",
                "Acquitted"
            ])

        })

        court_id += 1

    df = pd.DataFrame(rows)

    output="../data/generated"

    os.makedirs(output,exist_ok=True)

    df.to_csv(

        os.path.join(output,"court_cases.csv"),

        index=False

    )

    print(df.head())

    print(f"\nGenerated {len(df)} Court Cases")


if __name__=="__main__":

    generate_court_cases()