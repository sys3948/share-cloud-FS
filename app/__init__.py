from flask import Flask
from flask_cors import CORS
from config import config


cors = CORS()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    cors.init_app(app, resources={r'*': {'origins':'http://192.168.56.1:8000'}})

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app