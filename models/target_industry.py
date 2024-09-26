from db import db


class TargetIndustry(db.Model):
    __tablename__ = 'target_industries'
    id = db.Column(db.Integer, primary_key=True)
    industry = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'industry': self.industry
        }