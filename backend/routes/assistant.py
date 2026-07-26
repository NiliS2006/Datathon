from fastapi import APIRouter
from backend.database import db
import joblib
import pandas as pd
from pathlib import Path

router = APIRouter(tags=["Investigation Assistant"])

BASE = Path(__file__).resolve().parents[2]

model = joblib.load(BASE/"ml"/"priority_model.pkl")
encoders = joblib.load(BASE/"ml"/"label_encoders.pkl")


@router.post("/intelligence/analyze-case")
def analyze(data: dict):

    encoded = {}

    mapping = {
        "CrimeHeadName": data["Crime"],
        "DistrictName": data["District"],
        "StationName": data["PoliceStation"],
        "Weapon": data["Weapon"],
        "Vehicle": data["Vehicle"]
    }

    for feature,value in mapping.items():

        encoder = encoders[feature]

        if value not in encoder.classes_:
            value = encoder.classes_[0]

        encoded[feature]=encoder.transform([value])[0]

    X = pd.DataFrame([encoded])

    prediction = model.predict(X)[0]

    priority = encoders["Priority"].inverse_transform(
        [prediction]
    )[0]

    return {
        "Priority":priority
    }

    nearby = db["cases"].count_documents({

    "StationID":

    db["police_stations"].find_one({

        "StationName":data["PoliceStation"]

    })["StationID"]

})

similar = list(

    db["cases"].find(

        {

            "CrimeHeadID":

            db["crime_heads"].find_one({

                "CrimeHeadName":data["Crime"]

            })["CrimeHeadID"]

        },

        {

            "_id":0,

            "CaseID":1,

            "Status":1

        }

    ).limit(5)

)

risk = calculate_risk(
    data["District"]
)

return {

    "PredictedPriority":priority,

    "Confidence":confidence,

    "Risk":risk,

    "RecommendedOfficer":recommended,

    "NearbyCases":nearby,

    "SimilarCases":similar

}