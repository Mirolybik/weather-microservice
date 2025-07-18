from pydantic_settings import BaseSettings

class Settings(BaseSettings):  
    OPENWEATHERMAP_API_KEY: str  
    REDIS_URL: str = "redis://localhost:6379/0"  

    class Config:  
        env_file = ".env"  
        env_file_encoding = "utf-8"  

settings = Settings()  