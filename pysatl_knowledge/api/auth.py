from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from pysatl_knowledge.schemas.auth_schema import LoginResponse
from pysatl_knowledge.services.auth_service import AuthService
from pysatl_knowledge.services.dependencies import get_auth_service


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=LoginResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service),
):
    """
    Получить JWT токен.
    """
    token = await service.login(form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return token
