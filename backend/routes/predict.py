from pathlib import Path
import logging

import joblib
import pandas as pd
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["Prediction"])

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------
# Load trained model and encoders once during startup
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "ml" / "priority_model.pkl"
ENCODER_PATH = BASE_DIR / "ml" / "label_encoders.pkl"

try:
    model = joblib.load(MODEL_PATH)
    encoders = joblib.load(ENCODER_PATH)

except Exception as e:
    logger.exception("Unable to load ML model.")
    model = None
    encoders = None


# ---------------------------------------------------------------------
# Request Schema
# ---------------------------------------------------------------------

class PredictionRequest(BaseModel):
    Crime: str
    District: str
    PoliceStation: str
    Weapon: str
    Vehicle: str


# ---------------------------------------------------------------------
# Prediction Endpoint
# ---------------------------------------------------------------------

@router.post("/predict")
def predict(data: PredictionRequest):

    if model is None or encoders is None:
        raise HTTPException(
            status_code=500,
            detail="Prediction model is unavailable."
        )

    try:

        feature_mapping = {
            "CrimeHeadName": data.Crime,
            "DistrictName": data.District,
            "StationName": data.PoliceStation,
            "Weapon": data.Weapon,
            "Vehicle": data.Vehicle,
        }

        encoded = {}

        for feature, value in feature_mapping.items():

            if feature not in encoders:
                raise HTTPException(
                    status_code=500,
                    detail=f"Missing encoder for '{feature}'."
                )

            encoder = encoders[feature]

            # Handle unseen values
            if value not in encoder.classes_:
                value = encoder.classes_[0]

            encoded[feature] = encoder.transform([value])[0]

        X = pd.DataFrame([encoded])

        prediction = model.predict(X)[0]

        priority = encoders["Priority"].inverse_transform(
            [prediction]
        )[0]

        response = {
            "success": True,
            "predicted_priority": priority
        }

        # Confidence score if supported
        if hasattr(model, "predict_proba"):

            probability = model.predict_proba(X)[0]

            confidence = float(max(probability))

            response["confidence"] = round(confidence * 100, 2)

        return response

    except HTTPException:
        raise

    except Exception as e:

        logger.exception("Prediction failed.")

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )