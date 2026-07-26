import os
import pandas as pd

from master_data import CRIME_HEADS
def generate_crime_heads():
    rows = []
    for crime_id, crime_name in CRIME_HEADS.items():

        rows.append({

            "CrimeHeadID": crime_id,
            "CrimeHeadName": crime_name,
            "Status": "Active"

        })

    df = pd.DataFrame(rows)
    output_folder = os.path.join("..", "data", "generated")
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(
        output_folder,
        "crime_heads.csv"
    )

    df.to_csv(output_file, index=False)
    print("\nCrime Heads Generated Successfully!\n")
    print(df)
    print(f"\nSaved To : {output_file}")
    return df


if __name__ == "__main__":
    generate_crime_heads()