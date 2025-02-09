from flask import Flask

from .api.v1.endpoints import bp as api_bp
from .main.routes import bp as main_bp


def create_app():
    app = Flask(__name__)
    # app.config.from_object('app.config.Config')

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app
