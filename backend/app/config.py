import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL"
    )
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_SAMESITE = 'Lax'
    JWT_COOKIE_SECURE = False
    
