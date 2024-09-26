from db import db

class TargetCountry(db.Model):
    __tablename__ = 'target_countries'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), unique=True, nullable=True)
    cities = db.relationship('TargetCity', back_populates='target_country')

    def to_dict(self):
        return {
            'id': self.id,
            'country': self.country
        }