from db import db

class TargetCountry(db.Model):
    __tablename__ = 'target_country'
    country_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_name = db.Column(db.String(100), unique=True, nullable=False)
    cities = db.relationship('TargetCity', back_populates ='country')




    def to_dict(self):
        return {
            'country': self.country_name,
        }