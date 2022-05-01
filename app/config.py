from dotenv import find_dotenv, load_dotenv
import os
from pydantic import BaseSettings

load_dotenv(find_dotenv())

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    DATABASE_URL: str = os.getenv('DATABASE_URL')


settings = Settings()