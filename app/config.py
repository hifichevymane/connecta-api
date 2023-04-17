from pydantic import BaseSettings


# Validation of enviroment variables
class Settings(BaseSettings):
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # Connecting .env file
    class Config:
        env_file = ".env"

settings = Settings()
