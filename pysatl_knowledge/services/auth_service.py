from __future__ import annotations

from datetime import timedelta

from pysatl_knowledge.core.security.jwt_utils import create_access_token
from pysatl_knowledge.core.security.pass_utils import verify_password
from pysatl_knowledge.repositories import UserRepository
from pysatl_knowledge.schemas.auth_schema import LoginResponse


class AuthService:
    def __init__(self):
        self.repository = UserRepository()

    async def login(self, username: str, password: str) -> LoginResponse | None:
        # Находим пользователя
        user = await self.repository.find_by_username(username)
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None

        token = create_access_token({"sub": username}, expires_delta=timedelta(minutes=30))
        return LoginResponse(access_token=token)
