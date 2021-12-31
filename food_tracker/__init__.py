from flask import Flask
from .main.routes import food


def create_app():
    app = Flask(__name__)

    app.register_blueprint(food)

    return app