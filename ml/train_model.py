from pathlib import Path

import joblib
import pandas as pd
from pymongo import MongoClient

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# ============================================================
# Configuration
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "priority_model.pkl"
ENCODER_PATH = BASE_DIR / "label_encoders.pkl"

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "datathon"


# ============================================================
# MongoDB
# ============================================================

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

cases = pd.DataFrame(list(db["cases"].find()))
crime_heads = pd.DataFrame(list(db["crime_heads"].find()))
stations = pd.DataFrame(list(db["police_stations"].find()))

if cases.empty:
    raise RuntimeError("No case data found in MongoDB.")


# ============================================================
# Merge lookup collections
# ============================================================

cases = cases.merge(
    crime_heads[
        [
            "CrimeHeadID",
            "CrimeHeadName",
        ]
    ],
    on="CrimeHeadID",
    how="left",
)

cases = cases.merge(
    stations[
        [
            "StationID",
            "DistrictName",
            "StationName",
        ]
    ],
    on="StationID",
    how="left",
)


# ============================================================
# Select Features
# ============================================================

FEATURES = [
    "CrimeHeadName",
    "DistrictName",
    "StationName",
    "Weapon",
    "Vehicle",
]

TARGET = "Priority"

df = cases[FEATURES + [TARGET]].copy()

df = df.fillna("Unknown")
df = df.drop_duplicates()


# ============================================================
# Label Encoding
# ============================================================

encoders = {}

for column in FEATURES + [TARGET]:
    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    encoders[column] = encoder


# ============================================================
# Train/Test Split
# ============================================================

X = df[FEATURES]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)


# ============================================================
# Model
# ============================================================

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
)

model.fit(X_train, y_train)


# ============================================================
# Evaluation
# ============================================================

predictions = model.predict(X_test)

print("\nAccuracy")
print(accuracy_score(y_test, predictions))

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

print("\nFeature Importance")

importance = pd.DataFrame(
    {
        "Feature": FEATURES,
        "Importance": model.feature_importances_,
    }
)

importance = importance.sort_values(
    by="Importance",
    ascending=False,
)

print(importance)


# ============================================================
# Save Model
# ============================================================
print(MODEL_PATH)
print(ENCODER_PATH)
joblib.dump(model, MODEL_PATH)
joblib.dump(encoders, ENCODER_PATH)

print(f"\nModel saved to: {MODEL_PATH}")
print(f"Encoders saved to: {ENCODER_PATH}")

# ============================================================
# Save Model
# ============================================================

joblib.dump(model, MODEL_PATH)
joblib.dump(encoders, ENCODER_PATH)

print(f"\nModel saved to: {MODEL_PATH}")
print(f"Encoders saved to: {ENCODER_PATH}")

print("Model exists:", MODEL_PATH.exists())
print("Encoder exists:", ENCODER_PATH.exists())

print("Model size:", MODEL_PATH.stat().st_size)
print("Encoder size:", ENCODER_PATH.stat().st_size)