from flask import Blueprint, g, jsonify

bp = Blueprint('api', __name__)


@bp.route('/users', methods=['GET'])
def get_users():
    users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    return jsonify(users)


@bp.route('/set/<key>/<value>')
def set_redis_value(key, value):
    g.redis_client.set(key, value)  # This sets the value in Redis
    return jsonify({"message": f"Set {key} to {value} in Redis"})


@bp.route('/get/<key>')
def get_redis_value(key):
    return jsonify({"message": f"Get {key} to {str(g.redis_client.get(key))} in Redis"})
