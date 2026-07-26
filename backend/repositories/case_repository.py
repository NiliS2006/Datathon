from backend.database import db


def get_cases():

    return list(

        db["cases"].find(
            {},
            {"_id": 0}
        )

    )