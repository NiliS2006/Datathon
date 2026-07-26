import os
import pandas as pd
from master_data import CRIME_HEADS, CRIME_SUBHEADS


def generate_crime_subheads():
    rows = []
    subhead_id = 1
    for crime_head_id, crime_head_name in CRIME_HEADS.items():
        subheads = CRIME_SUBHEADS.get(crime_head_name, [])
        for subhead in subheads:
            rows.append({
                "CrimeSubHeadID": subhead_id,
                "CrimeHeadID": crime_head_id,
                "CrimeHeadName": crime_head_name,
                "CrimeSubHeadName": subhead,
                "Status": "Active"

            })
            subhead_id += 1

    df = pd.DataFrame(rows)
    output_folder = os.path.join("..", "data", "generated")
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(
        output_folder,
        "crime_subheads.csv"
    )
    df.to_csv(output_file, index=False)
    print("\nCrime Sub Heads Generated Successfully!\n")
    print(df)
    print(f"\nTotal Crime Sub Heads : {len(df)}")
    print(f"\nSaved To : {output_file}")
    return df


if __name__ == "__main__":
    generate_crime_subheads()