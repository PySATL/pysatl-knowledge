# app/services/auth_service.py
from __future__ import annotations

from datetime import timedelta

from pysatl_knowledge.core.moke_db import MOCK_USERS
from pysatl_knowledge.core.security import create_access_token
from pysatl_knowledge.schemas.auth import LoginResponse


class AuthService:
    async def login(self, username: str, password: str) -> LoginResponse | None:
        user = MOCK_USERS.get(username)
        if not user or user["password"] != password:
            return None
        token = create_access_token({"sub": username}, expires_delta=timedelta(minutes=30))
        return LoginResponse(access_token=token)
