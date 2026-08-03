import os


class Config:
    FT_CLIENT_ID = os.getenv("FT_CLIENT_ID")
    FT_CLIENT_SECRET = os.getenv("FT_CLIENT_SECRET")
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "development-key")