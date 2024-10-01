from db import db


class TargetIndustry(db.Model):
    __tablename__ = 'target_industry'
    industry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    industry_name = db.Column(db.String(100), nullable=False, unique=True)
    targets = db.relationship('Target', back_populates='industry')




    def to_dict(self):
        return  self.industry_name