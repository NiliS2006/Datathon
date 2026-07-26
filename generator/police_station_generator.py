import os
import random
import pandas as pd

from master_data import DISTRICTS, POLICE_STATIONS

def get_officer_count(station_type):
    """Generate officers based on station type."""

    if station_type == "Urban":
        return random.randint(60, 120)

    elif station_type == "Semi Urban":
        return random.randint(40, 80)

    else:
        return random.randint(20, 50)


def get_annual_cases(station_type):

    if station_type == "Urban":
        return random.randint(1800, 4500)

    elif station_type == "Semi Urban":
        return random.randint(800, 1800)

    else:
        return random.randint(200, 800)


def generate_police_stations():

    rows = []

    station_id = 1

    for district_name, stations in POLICE_STATIONS.items():

        district = DISTRICTS[district_name]

        for station in stations:

            latitude = round(
                district["latitude"] + random.uniform(-0.04, 0.04),
                6
            )

            longitude = round(
                district["longitude"] + random.uniform(-0.04, 0.04),
                6
            )

            rows.append({

                "StationID": station_id,
                "StationName": station["name"],
                "DistrictID": district["id"],
                "DistrictName": district_name,
                "StationType": station["type"],
                "Latitude": latitude,
                "Longitude": longitude,
                "OfficerCount": get_officer_count(station["type"]),
                "AnnualCases": get_annual_cases(station["type"]),
                "Status": "Active"

            })

            station_id += 1

    df = pd.DataFrame(rows)

    output_folder = os.path.join("..", "data", "generated")
    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(
        output_folder,
        "police_stations.csv"
    )

    df.to_csv(output_file, index=False)
    print("\nPolice Stations Generated Successfully!\n")
    print(df)
    print(f"\nTotal Stations : {len(df)}")
    print(f"\nSaved To : {output_file}")

    return df


if __name__ == "__main__":
    generate_police_stations()