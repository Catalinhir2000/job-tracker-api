from flask import Flask
from app.config import Config
from app.extensions import db, migrate, ma

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from app.models import User, Company, Application  # Import models to register them with SQLAlchemy

    @app.route("/")
    def index():
        return "message: Job Tracker API is running!"

    return app