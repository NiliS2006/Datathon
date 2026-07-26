from fastapi import APIRouter, HTTPException, Query
from backend.services.case_service import (
    get_all_cases,
    get_case
)

router = APIRouter(tags=["Cases"])


@router.get("/cases")
def cases(
    limit: int = Query(100, ge=1, le=1000),
    skip: int = Query(0, ge=0)
):
    """
    Get all cases with pagination.
    """

    try:
        return get_all_cases(limit=limit, skip=skip)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unable to fetch cases: {str(e)}"
        )


@router.get("/cases/{case_id}")
def case(case_id: int):
    """
    Get a single case by CaseID.
    """

    try:

        result = get_case(case_id)

        if result is None:
            raise HTTPException(
                status_code=404,
                detail=f"Case {case_id} not found"
            )

        return result

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unable to fetch case: {str(e)}"
        )