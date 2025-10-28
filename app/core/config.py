from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI VIP Example"
    DEBUG: bool = True
    ENV: str = 'dev'
    VERSION: str = '0.0.1'

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

settings = Settings()