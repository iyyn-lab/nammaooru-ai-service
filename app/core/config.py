from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Namma Ooru AI Service"
    app_env: str = "dev"
    debug: bool = True

    aws_region: str = "ap-south-1"

    llm_provider: str = ""
    llm_model: str = ""
    llm_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()