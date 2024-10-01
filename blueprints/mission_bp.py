from flask import Blueprint, jsonify
from services.mission_service import get_all_targets, get_target_by_id

mission_bp = Blueprint('mission_bp', __name__, url_prefix='/api')


@mission_bp.route('/mission', methods=['GET'])
def get_mission():
    data = get_all_targets()
    targets = [target.to_dict() for target in data]
    return jsonify(targets)




@mission_bp.route('/mission/<int:mission_id>', methods=['GET'])
def get_mission_by_id(mission_id):
    data = get_target_by_id(mission_id)
    return jsonify(data.to_dict())