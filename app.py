from flask import Flask, Blueprint
from blueprints.mission_bp import mission_bp
from db import db
from models.target import Target
from models.target_city import TargetCity
from models.target_country import TargetCountry


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/wwii_missions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

app.register_blueprint(mission_bp)


with app.app_context():
    db.drop_all()
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True)