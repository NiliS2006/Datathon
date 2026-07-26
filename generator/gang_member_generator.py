import os
import random
import pandas as pd


def generate_gang_members():

    gangs = pd.read_csv("../data/generated/gangs.csv")

    history = pd.read_csv("../data/generated/criminal_history.csv")

    criminals = history["PersonID"].drop_duplicates().tolist()

    rows = []

    membership_id = 1

    for gang in gangs.itertuples():

        member_count = random.randint(5, 20)

        if len(criminals) < member_count:
            selected = criminals
        else:
            selected = random.sample(criminals, member_count)

        leader = random.choice(selected)

        for person in selected:

            rows.append({

                "MembershipID": membership_id,

                "GangID": gang.GangID,

                "PersonID": person,

                "Role": "Leader" if person == leader else "Member",

                "JoinYear": random.randint(2015, 2025)

            })

            membership_id += 1

    df = pd.DataFrame(rows)

    output = "../data/generated"

    os.makedirs(output, exist_ok=True)

    df.to_csv(

        os.path.join(output, "gang_members.csv"),

        index=False

    )

    print(df.head())

    print()

    print(f"Generated {len(df)} Gang Memberships")

    return df


if __name__ == "__main__":

    generate_gang_members()