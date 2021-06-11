import os

BASE_DIR = dirname(dirname(abspath(__file__)))
TESTING = False
DEBUG = False
SQLALCHEMY_DATABASE_URI = os.getenv("APP_WEB_DB")
SQLALCHEMY_TRACK_MODIFICATIONS = False
MONGODB_HOST = os.getenv("APP_WEB_MONGO")
