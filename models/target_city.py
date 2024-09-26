from db import db
from models.target_country import TargetCountry


class TargetCity(db.Model):
    __tablename__ = 'target_cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country_id = db.Column(db.Integer, db.ForeignKey('target_countries.id'))
    country = db.relationship('TargetCountry', back_populates ='cities')

    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'country_id': self.country_id,
            'country': self.country
        }