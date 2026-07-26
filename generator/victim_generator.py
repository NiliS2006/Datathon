import os
import random
import pandas as pd


def generate_case_victims():

    cases = pd.read_csv("../data/generated/case_master.csv")

    persons = pd.read_csv("../data/generated/persons.csv")

    rows = []

    record_id = 1

    for _, case in cases.iterrows():

        victim_count = random.randint(1, 3)

        victims = persons.sample(victim_count)

        for _, victim in victims.iterrows():

            rows.append({

                "RecordID": record_id,

                "CaseID": case["CaseID"],

                "PersonID": victim["PersonID"],

                "VictimType": random.choice([
                    "Primary",
                    "Secondary"
                ])

            })

            record_id += 1

    df = pd.DataFrame(rows)

    output = "../data/generated"

    os.makedirs(output, exist_ok=True)

    df.to_csv(
        os.path.join(output, "case_victims.csv"),
        index=False
    )

    print(df.head())

    print(f"\nGenerated {len(df)} Case Victims")


if __name__ == "__main__":

    generate_case_victims()