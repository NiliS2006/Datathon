import os
import random
import pandas as pd

from master_data import GANG_NAMES, GANG_TYPES


def generate_gangs(number_of_gangs=50):

    rows = []

    for gang_id in range(1, number_of_gangs + 1):

        rows.append({

            "GangID": gang_id,

            "GangName": random.choice(GANG_NAMES) + f" {gang_id}",

            "GangType": random.choice(GANG_TYPES),

            "FormationYear": random.randint(1990, 2023),

            "ActiveStatus": random.choice([
                "Active",
                "Inactive"
            ])

        })

    df = pd.DataFrame(rows)

    output = "../data/generated"

    os.makedirs(output, exist_ok=True)

    df.to_csv(

        os.path.join(output, "gangs.csv"),

        index=False

    )

    print(df.head())

    print()

    print(f"Generated {len(df)} Gangs")

    return df


if __name__ == "__main__":

    generate_gangs()