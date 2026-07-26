import os
import random
import pandas as pd

from master_data import ARREST_STATUS


def generate_criminal_history():

    persons = pd.read_csv("../data/generated/persons.csv")
    cases = pd.read_csv("../data/generated/case_master.csv")

    rows = []

    history_id = 1

    # About 15% of people have previous records
    criminals = persons.sample(frac=0.15, random_state=42)

    for _, person in criminals.iterrows():

        previous_cases = random.randint(1, 6)

        sampled_cases = cases.sample(previous_cases)

        for _, case in sampled_cases.iterrows():

            convicted = random.choice([True, False])

            sentence = random.randint(1, 20) if convicted else 0

            rows.append({

                "HistoryID": history_id,

                "PersonID": person["PersonID"],

                "CaseID": case["CaseID"],

                "ArrestStatus": random.choice(ARREST_STATUS),

                "Convicted": convicted,

                "SentenceYears": sentence,

                "RepeatOffender": previous_cases > 2

            })

            history_id += 1

    df = pd.DataFrame(rows)

    output = "../data/generated"

    os.makedirs(output, exist_ok=True)

    df.to_csv(

        os.path.join(output, "criminal_history.csv"),

        index=False

    )

    print(df.head())

    print()

    print(f"Generated {len(df)} Criminal Records")

    return df


if __name__ == "__main__":

    generate_criminal_history()