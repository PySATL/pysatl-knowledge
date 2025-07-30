from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "test"
    secret_key: str = "supersecretkey"
    access_token_expire_minutes: int = 30
    log_level: str = "INFO"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "test"
    DB_USER: str = "test"
    DB_PASS: str = "<PASSWORD>"

    class Config:
        env_file = ".env"
        extra = "ignore"

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:"
            f"{self.DB_PASS}@"
            f"{self.DB_HOST}:"
            f"{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )


settings = Settings()
