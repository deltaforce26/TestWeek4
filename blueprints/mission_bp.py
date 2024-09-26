from flask import Blueprint, jsonify

from models.target import Target

mission_bp = Blueprint('mission_bp', __name__, url_prefix='/api')


@mission_bp.route('/mission', methods=['GET'])
def get_mission():
    data = Target.query.all()
    targets = [target.to_dict() for target in data]
    return jsonify(targets)




@mission_bp.route('/mission/<int:mission_id>', methods=['GET'])
def get_mission_by_id(mission_id):
    pass