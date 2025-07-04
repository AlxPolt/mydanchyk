from fastapi import APIRouter

router = APIRouter(prefix="/courts", tags=["courts"])

@router.get("/")
def get_courts():
    return [{"id": 1, "name": "Racket Sports Park", "city": "Kyiv", "is_adaptive": True}]
