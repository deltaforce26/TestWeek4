from db import db

class TargetType(db.Model):
    __tablename__ = 'target_type'
    type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(100), nullable=True)
    targets = db.relationship('Target', back_populates='type')

    def to_dict(self):
        return self.type_name