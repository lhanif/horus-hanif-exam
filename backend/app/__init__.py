from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, cors
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, supports_credentials=True)
    
    register_routes(app)

    return app