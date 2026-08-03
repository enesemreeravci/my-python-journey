from flask import Flask
from dotenv import load_dotenv

from config import Config

def create_app() -> Flask:
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import main
    app.register_blueprint(main)

    return app
