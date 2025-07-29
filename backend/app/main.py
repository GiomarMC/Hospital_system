from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.config import settings

jwt = JWTManager()


def create_app():
    app = Flask(__name__)

    # Configuracion de JWT desde settings
    app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = settings.JWT_ACCESS_TOKEN_EXPIRES
    app.config['SECRET_KEY'] = settings.SECRET_KEY

    CORS(app, supports_credentials=True)
    jwt.init_app(app)

    return app