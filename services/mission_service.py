from models.target import Target


def get_all_targets():
    targets = Target.query.all()
    return targets


def get_target_by_id(target_id):
    target = Target.query.filter_by(target_id=target_id).first()
    return target
