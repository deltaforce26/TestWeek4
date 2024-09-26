from db import db

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(80), unique=True, nullable=True)


    def to_dict(self):
        return {
            'id': self.id,
            'country': self.country
        }