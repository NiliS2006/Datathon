import os
import random
import pandas as pd


def generate_witnesses():

    cases = pd.read_csv("../data/generated/case_master.csv")
    persons = pd.read_csv("../data/generated/persons.csv")

    rows = []

    witness_id = 1

    for _, case in cases.iterrows():

        number = random.randint(0, 4)

        if number == 0:
            continue

        witnesses = persons.sample(number)

        for _, witness in witnesses.iterrows():

            rows.append({

                "WitnessID": witness_id,

                "CaseID": case["CaseID"],

                "PersonID": witness["PersonID"],

                "WitnessType": random.choice([
                    "Eye Witness",
                    "Expert Witness",
                    "Circumstantial Witness"
                ]),

                "StatementRecorded": random.choice([
                    True,
                    False
                ])

            })

            witness_id += 1

    df = pd.DataFrame(rows)

    output = "../data/generated"

    os.makedirs(output, exist_ok=True)

    df.to_csv(
        os.path.join(output, "witnesses.csv"),
        index=False
    )

    print(df.head())
    print(f"\nGenerated {len(df)} Witness Records")


if __name__ == "__main__":

    generate_witnesses()