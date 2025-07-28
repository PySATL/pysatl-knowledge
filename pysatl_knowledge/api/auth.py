from fastapi import APIRouter


router = APIRouter(prefix="/hello", tags=["Hello"])


@router.get("")
async def say_hello():
    return {"message": "Hello World!"}
