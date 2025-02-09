import os


class Config:
    APP_NAME = os.getenv('APP_NAME', 'Amatsuriki')
    DATABASE_URL = os.getenv('DATABASE_URL')
    REDIS_URL = os.getenv('REDIS_URL')
