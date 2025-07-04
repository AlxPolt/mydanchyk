from fastapi import APIRouter, Query
from ml.recommendations import get_recommendations

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

@router.get("/")
def recommend(user_id: int = Query(...)):
    return get_recommendations(user_id)
