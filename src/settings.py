from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env")

    db_name: str = "db_name"
    db_user: str = "db_user"
    db_host: str = "db_host"
    db_port: str = "db_port"
    db_pass: str = "db_pass"

    def get_db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}"


settings = Settings()

