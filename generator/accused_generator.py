import os
import random
import pandas as pd


def generate_case_accused():

    cases = pd.read_csv("../data/generated/case_master.csv")

    persons = pd.read_csv("../data/generated/persons.csv")

    rows = []

    record_id = 1

    for _, case in cases.iterrows():

        accused_count = random.randint(1, 4)

        accused = persons.sample(accused_count)

        for _, person in accused.iterrows():

            rows.append({

                "RecordID": record_id,

                "CaseID": case["CaseID"],

                "PersonID": person["PersonID"],

                "Role": random.choice([
                    "Main Accused",
                    "Co-Accused"
                ])

            })

            record_id += 1

    df = pd.DataFrame(rows)

    output = "../data/generated"

    os.makedirs(output, exist_ok=True)

    df.to_csv(

        os.path.join(output, "case_accused.csv"),

        index=False

    )

    print(df.head())

    print(f"\nGenerated {len(df)} Case Accused")


if __name__ == "__main__":

    generate_case_accused()