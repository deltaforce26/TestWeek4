from db import db

class TargetType(db.Model):
    __tablename__ = 'target_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=True)


    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type
        }