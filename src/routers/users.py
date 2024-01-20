from fastapi import APIRouter

router = APIRouter()


# TODO: remove this example function
@router.get("/")
def read_users():
    return [{"username": "mewtwo", "demographic": {}}]
