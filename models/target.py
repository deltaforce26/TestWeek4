from db import db


class Target(db.Model):
    __tablename__ = 'target'

    id = db.Column(db.Integer, primary_key=True)

    target_city = db.Column(db.Integer, db.ForeignKey('target_cities.id'), nullable=True)
    target_industry = db.Column(db.Integer, db.ForeignKey('target_industries.id'), nullable=True)
    target_type = db.Column(db.Integer, db.ForeignKey('target_types.id'), nullable=True)

    target_latitude = db.Column(db.Numeric(10, 6), nullable=True)
    target_longitude = db.Column(db.Numeric(10, 6), nullable=True)
    city = db.relationship('TargetCity', back_populates ='targets', lazy=True)
    industry = db.relationship('TargetIndustry', back_populates ='targets', lazy=True)
    type = db.relationship('TargetType', back_populates ='targets', lazy=True)



    def to_dict(self):
        return {
            'id': self.id,
            'target_city': self.target_city,
            'target_country': self.target_city.country,
            'target_industry': self.target_industry,
            'target_type': self.target_type,
            'target_latitude': self.target_latitude,
            'target_longitude': self.target_longitude
        }