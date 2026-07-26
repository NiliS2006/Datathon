from fastapi import APIRouter
import random

router = APIRouter(tags=["Resolution"])


@router.get("/predict/resolution-days")
def resolution(priority: str):

    estimates = {

        "High": random.randint(10,20),

        "Medium": random.randint(20,35),

        "Low": random.randint(30,60)

    }

    return {

        "EstimatedResolutionDays":

        estimates.get(priority,30)

    }