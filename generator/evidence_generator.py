import os
import random
import pandas as pd

from master_data import (
    EVIDENCE_TYPES,
    EVIDENCE_STATUS
)


def generate_evidence():

    cases = pd.read_csv("../data/generated/case_master.csv")

    rows = []

    evidence_id = 1

    for _, case in cases.iterrows():

        evidence_count = random.randint(1, 5)

        selected = random.sample(
            EVIDENCE_TYPES,
            evidence_count
        )

        for evidence in selected:

            rows.append({

                "EvidenceID": evidence_id,

                "CaseID": case["CaseID"],

                "EvidenceType": evidence,

                "CollectedDate": case["Date"],

                "Status": random.choice(EVIDENCE_STATUS),

                "ForensicLab": random.choice([
                    "Bengaluru FSL",
                    "Mysuru FSL",
                    "Mangaluru FSL"
                ]),

                "Verified": random.choice([
                    True,
                    False
                ])

            })

            evidence_id += 1

    df = pd.DataFrame(rows)

    output = "../data/generated"

    os.makedirs(output, exist_ok=True)

    df.to_csv(

        os.path.join(output, "evidence.csv"),

        index=False

    )

    print(df.head())

    print()

    print(f"Generated {len(df)} Evidence Records")

    return df


if __name__ == "__main__":

    generate_evidence()