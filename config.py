from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MSTR_BASE_URL: str
    MSTR_USERNAME: str
    MSTR_PASSWORD: str
    MSTR_PROJECT_ID: str = ""
    VERIFY_SSL: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()