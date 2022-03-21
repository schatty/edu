from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+pg8000://app:password@localhost/shop"
)

class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = None
    ENV = "development"

    SECRET_KEY="abc"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = "production"
    SECRET_KEY = "qwerty"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True