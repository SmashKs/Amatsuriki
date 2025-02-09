from flask import Blueprint, jsonify

bp = Blueprint('api', __name__)


@bp.route('/users', methods=['GET'])
def get_users():
    users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    return jsonify(users)
