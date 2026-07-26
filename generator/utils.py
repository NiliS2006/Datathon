import random
import string
from datetime import datetime, timedelta


def generate_fir_number(case_id):
    year = random.randint(2022, 2026)
    return f"FIR/{year}/{case_id:06d}"


def random_date(start_year=2022, end_year=2026):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


def generate_phone():
    return "9" + "".join(random.choices(string.digits, k=9))

def random_gender():
    return random.choice(["Male", "Female"])

def random_status():
    return random.choice([
        "Pending",
        "Charge Sheet Filed",
        "Closed",
        "Under Investigation"
    ])

def random_coordinates(lat, lon):
    latitude = round(lat + random.uniform(-0.03, 0.03), 6)
    longitude = round(lon + random.uniform(-0.03, 0.03), 6)
    return latitude, longitude