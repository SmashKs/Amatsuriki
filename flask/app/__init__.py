import redis
from flask import Flask, g
from flask_cors import CORS

from .api.v1.endpoints import bp as api_bp
from .config import Config
from .main.routes import bp as main_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load configuration
    app.config.from_object(Config)

    # Use a before_request handler to initialize Redis
    @app.before_request
    def before_request():
        g.redis_client = redis.from_url(app.config['REDIS_URL'])

    @app.teardown_appcontext
    def teardown_redis(exception):
        if hasattr(g, 'redis_client'):
            g.redis_client.close()

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app
