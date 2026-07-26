import os
import random
import pandas as pd

from master_data import (
    VEHICLE_TYPES,
    VEHICLE_COLORS,
    VEHICLE_BRANDS
)


def registration_number():

    districts = [
        "KA01", "KA02", "KA03", "KA04",
        "KA05", "KA09", "KA11", "KA19"
    ]

    return (
        random.choice(districts)
        + chr(random.randint(65, 90))
        + chr(random.randint(65, 90))
        + str(random.randint(1000, 9999))
    )


def generate_vehicles():

    persons = pd.read_csv("../data/generated/persons.csv")

    rows = []

    vehicle_id = 1

    for _, person in persons.iterrows():

        if random.random() < 0.60:

            number_of_vehicles = random.randint(1, 2)

            for _ in range(number_of_vehicles):

                rows.append({

                    "VehicleID": vehicle_id,

                    "RegistrationNumber": registration_number(),

                    "OwnerPersonID": person["PersonID"],

                    "VehicleType": random.choice(VEHICLE_TYPES),

                    "Brand": random.choice(VEHICLE_BRANDS),

                    "Color": random.choice(VEHICLE_COLORS),

                    "ManufactureYear": random.randint(2008, 2025),

                    "IsStolen": random.choice([
                        False,
                        False,
                        False,
                        True
                    ])

                })

                vehicle_id += 1

    df = pd.DataFrame(rows)

    output = "../data/generated"

    os.makedirs(output, exist_ok=True)

    df.to_csv(

        os.path.join(output, "vehicles.csv"),

        index=False

    )

    print(df.head())

    print()

    print(f"Generated {len(df)} Vehicles")

    return df


if __name__ == "__main__":

    generate_vehicles()