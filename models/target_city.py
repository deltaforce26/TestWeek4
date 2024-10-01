from db import db



class TargetCity(db.Model):
    __tablename__ = 'target_city'

    city_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('target_country.country_id'))
    country = db.relationship('TargetCountry', back_populates ='cities')
    targets = db.relationship('Target', back_populates='city')





    def to_dict(self):
        return self.city_name, self.country.to_dict()