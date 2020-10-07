from os.path import abspath, dirname, join

BASE_DIR = dirname(dirname(abspath(__file__)))
TESTING = True
DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///testing.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
MONGODB_DB = 'testing'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
