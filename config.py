import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/farmers_database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPEN_WEATHER_APIKEY = os.environ.get("OPEN_WEATHER_APIKEY")
    HUGGINGFACE_LOGIN_TOKEN = os.environ.get("HUGGINGFACE_LOGIN_TOKEN")