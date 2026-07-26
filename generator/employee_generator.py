import os
import random
import pandas as pd
from faker import Faker
from master_data import OFFICER_RANKS
from master_data import DEPARTMENTS

fake = Faker("en_IN")
def generate_employees():
    stations = pd.read_csv("../data/generated/police_stations.csv")
    rows = []
    employee_id = 100001
    for _, station in stations.iterrows():
        officer_count = int(station["OfficerCount"])
        for _ in range(officer_count):
            rows.append({
                "EmployeeID": employee_id,
                "OfficerName": fake.name(),
                "Rank": random.choice(OFFICER_RANKS),
                "Department": random.choice(DEPARTMENTS),
                "Phone": fake.phone_number(),
                "Email": fake.email(),
                "JoiningYear": random.randint(1995, 2025),
                "StationID": station["StationID"],
                "StationName": station["StationName"],
                "DistrictID": station["DistrictID"],
                "DistrictName": station["DistrictName"],
                "Status": "Active"

            })
            employee_id += 1
    df = pd.DataFrame(rows)
    output_folder = "../data/generated"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(
        output_folder,
        "employees.csv"
    )
    df.to_csv(output_file, index=False)
    print(df.head())
    print()
    print(f"Generated {len(df)} Employees")

    print(f"Saved to {output_file}")

    return df


if __name__ == "__main__":

    generate_employees()