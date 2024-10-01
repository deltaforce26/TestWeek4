from db import db


class Target(db.Model):
    __tablename__ = 'target'

    target_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_id = db.Column(db.Integer, db.ForeignKey('target_city.city_id'))
    city = db.relationship('TargetCity', back_populates='targets', lazy="joined")
    industry_id = db.Column(db.Integer, db.ForeignKey('target_industry.industry_id'))
    industry = db.relationship('TargetIndustry', back_populates='targets', lazy="joined")
    type_id = db.Column(db.Integer, db.ForeignKey('target_type.type_id'))
    type = db.relationship('TargetType', back_populates='targets', lazy="joined")
    target_priority = db.Column(db.String(100))
    target_latitude = db.Column(db.Numeric(10, 6), nullable=True)
    target_longitude = db.Column(db.Numeric(10, 6), nullable=True)






    def to_dict(self):
        return {
            'id': self.target_id,
            'city': self.city.to_dict(),
            'industry': self.industry.to_dict(),
            'type': self.type.to_dict(),
            'latitude': self.target_latitude,
            'longitude': self.target_longitude
        }