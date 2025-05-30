from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    AUTH_SECRET: str
    AUTH_ALGORITHM: str
    AUTH_TOKEN_EXPIRATION_MINUTES: int

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
