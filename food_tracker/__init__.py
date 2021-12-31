from flask import Flask
from 


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "test"

    return app