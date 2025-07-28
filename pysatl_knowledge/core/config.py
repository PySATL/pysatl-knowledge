from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "test"
    secret_key: str = "supersecretkey"
    access_token_expire_minutes: int = 30
    log_level: str = "INFO"
    database_url: str = "mock://user:pass@localhost:5432/dbname"
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    class Config:
        env_file = ".env"
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
