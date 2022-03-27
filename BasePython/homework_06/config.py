from os import getenv


SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+pg8000://app:password@localhost/shop"
)


class Config:
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY="abc"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    ENV = "production"