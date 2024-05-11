from flask import Flask
from .routes import system_info

def create_app():
    app = Flask(__name__)
    app.register_blueprint(system_info)
    return app
