from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response, status_code = register_user(data)  # Descompacta a resposta e o código de status
    return jsonify(response), status_code

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response, status_code = login_user(data)
    return jsonify(response), status_code
