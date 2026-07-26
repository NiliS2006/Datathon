import os
import random
import pandas as pd
from faker import Faker
from master_data import DISTRICTS
from master_data import OCCUPATIONS
from master_data import RELIGIONS
from master_data import MARITAL_STATUS
from master_data import EDUCATION

fake = Faker("en_IN")

def generate_people(number_of_people=25000):
    rows = []
    person_id = 500001
    district_names = list(DISTRICTS.keys())
    for _ in range(number_of_people):
        district = random.choice(district_names)
        rows.append({
            "PersonID": person_id,
            "Name": fake.name(),
            "Gender": random.choice(["Male","Female"]),
            "Age": random.randint(18,75),
            "Religion": random.choice(RELIGIONS),
            "Occupation": random.choice(OCCUPATIONS),
            "Education": random.choice(EDUCATION),
            "MaritalStatus": random.choice(MARITAL_STATUS),
            "Phone": fake.phone_number(),
            "Address": fake.address().replace("\n"," "),
            "District": district
        })

        person_id += 1
    df = pd.DataFrame(rows)
    output_folder="../data/generated"
    os.makedirs(output_folder,exist_ok=True)
    df.to_csv(
        os.path.join(output_folder,"persons.csv"),
        index=False
    )

    print(df.head())
    print()
    print(f"Generated {len(df)} Persons")
    return df

if __name__=="__main__":

    generate_people()