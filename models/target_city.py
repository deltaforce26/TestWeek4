from  db import db


class TargetCity(db.Model):
    __tablename__ = 'target_cities'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), unique=True, nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('target_countries.id'))
    country = db.relationship('TargetCountry', back_populates='target_city')


    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'country_id': self.country_id,
            'country': self.country
        }