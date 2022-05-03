from dotenv import find_dotenv, load_dotenv
import os
import re
from pydantic import BaseSettings

load_dotenv(find_dotenv())


uri = os.getenv("DATABASE_TYPE")


class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    # SQL_DATABASE_URL: str = uri.replace("postgres://", "postgresql://", 1) if uri.startswith("postgres://") else uri
    DATABASE_TYPE: str = uri.replace("postgres://", "postgresql://", 1) if uri.startswith("postgres://") else uri
    DATABASE_PORT: int = os.getenv('DATABASE_PORT')
    DATABASE_PASSWORD: str = os.getenv('DATABASE_PASSWORD')
    DATABASE_NAME: str = os.getenv('DATABASE_NAME')
    DATABASE_USERNAME: str = os.getenv('DATABASE_USERNAME')
    DATABASE_HOSTNAME: str = os.getenv('DATABASE_HOSTNAME')


settings = Settings()
