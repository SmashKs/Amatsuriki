import os

import psycopg2
import redis
from flask import Flask, g
from flask_cors import CORS

from .api.v1.endpoints import bp as api_bp
from .config import Config
from .main.routes import bp as main_bp


def get_db_connection():
    """
    Create and return a PostgreSQL database connection.
    :return: connection object
    """
    return psycopg2.connect(os.getenv('DATABASE_URL'))  # Get Database URL from environment


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load configuration
    app.config.from_object(Config)

    # Use a before_request handler to initialize Redis
    @app.before_request
    def before_request():
        g.redis_client = redis.from_url(app.config['REDIS_URL'])
        g.db_conn = get_db_connection()  # Initialize database connection

    @app.teardown_appcontext
    def teardown_redis(exception):
        if hasattr(g, 'redis_client'):
            del g.redis_client  # Not necessary to close, as redis-py handles connection pools

        # Close PostgreSQL database connection
        if hasattr(g, 'db_conn'):
            g.db_conn.close()

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app
