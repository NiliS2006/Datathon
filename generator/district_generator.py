import os
import pandas as pd

from master_data import DISTRICTS

def generate_districts():
    rows = []
    for district_name, details in DISTRICTS.items():

        row = {
            "DistrictID": details["id"],
            "DistrictName": district_name,
            "Population": details["population"],
            "Literacy": details["literacy"],
            "Urbanization": details["urban"],
            "Latitude": details["latitude"],
            "Longitude": details["longitude"]
        }
        rows.append(row)

         # Convert list of dictionaries into a DataFrame
    df = pd.DataFrame(rows)
    # Create output folder if it doesn't exist
    output_folder = os.path.join("..", "data", "generated")
    os.makedirs(output_folder, exist_ok=True)
    # Save CSV
    output_path = os.path.join(output_folder, "districts.csv")
    df.to_csv(output_path, index=False)
    print("\nDistrict Dataset Generated Successfully!\n")
    print(df)

    return df

if __name__ == "__main__":
    generate_districts()

