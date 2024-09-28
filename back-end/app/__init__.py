from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_cors import CORS
# Instancia as extensões sem inicializá-las ainda
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}}, methods=["GET", "POST", "PUT", "DELETE"])
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Registra as rotas
    with app.app_context():
        from app.routes import create, list, update

    return app
