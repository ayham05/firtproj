from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    sql_url:str = "postgresql://postgres....."
    SECRET_KEY:str = "jkdsjk-sfgfdd-fgdfgf"
    ALGORITHM:str  = "HS256"
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()