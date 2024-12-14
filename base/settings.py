
from pydantic_settings import BaseSettings


class SSettings(BaseSettings):
    database_url: str

    class Config:
        extra = "allow"
        env_file = f"./.env"

Settings=SSettings()