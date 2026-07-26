from fastapi import APIRouter, HTTPException
from backend.database import db

router = APIRouter(tags=["Risk Intelligence"])


@router.get("/intelligence/risk-score")
def risk_scores():

    try:

        pipeline = [

            {
                "$group": {

                    "_id": "$DistrictName",

                    "TotalCases": {
                        "$sum": 1
                    },

                    "PendingCases": {
                        "$sum": {
                            "$cond": [
                                {
                                    "$eq": [
                                        "$Status",
                                        "Pending"
                                    ]
                                },
                                1,
                                0
                            ]
                        }
                    },

                    "HighPriority": {
                        "$sum": {
                            "$cond": [
                                {
                                    "$eq": [
                                        "$Priority",
                                        "High"
                                    ]
                                },
                                1,
                                0
                            ]
                        }
                    }

                }
            }

        ]

        districts = list(db["cases"].aggregate(pipeline))

        response = []

        for district in districts:

            total = district["TotalCases"]

            pending = district["PendingCases"]

            high = district["HighPriority"]

            pending_score = (pending / total) * 40 if total else 0

            priority_score = (high / total) * 60 if total else 0

            risk_score = round(
                pending_score + priority_score,
                2
            )

            if risk_score >= 80:
                level = "Critical"

            elif risk_score >= 60:
                level = "High"

            elif risk_score >= 40:
                level = "Medium"

            else:
                level = "Low"

            recommendation = []

            if pending > 30:
                recommendation.append(
                    "Increase investigating officers"
                )

            if high > 20:
                recommendation.append(
                    "Deploy additional patrol units"
                )

            if not recommendation:
                recommendation.append(
                    "Current deployment is sufficient"
                )

            response.append(

                {

                    "District": district["_id"],

                    "RiskScore": risk_score,

                    "RiskLevel": level,

                    "TotalCases": total,

                    "PendingCases": pending,

                    "HighPriorityCases": high,

                    "Recommendation": recommendation

                }

            )

        response.sort(

            key=lambda x: x["RiskScore"],

            reverse=True

        )

        return {

            "success": True,

            "districts": response

        }

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )