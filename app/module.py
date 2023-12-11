from fastapi import APIRouter

router = APIRouter()


@router.get("/modping")
def ping():
    return {"modping": "pong!"}
