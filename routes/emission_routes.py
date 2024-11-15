from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.emission_service import calculate_emission, get_emission_history

emission_bp = Blueprint('emission', __name__)

@emission_bp.route('/', methods=['POST'])
@jwt_required()
def add_emission():
    data = request.get_json()
    user_id = get_jwt_identity()
    response = calculate_emission(user_id, data)
    return jsonify(response), 201

@emission_bp.route('/history', methods=['GET'])
@jwt_required()
def history():
    user_id = get_jwt_identity()
    response = get_emission_history(user_id)
    return jsonify(response), 200
