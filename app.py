from flask import Flask
from blueprints.mission_bp import mission_bp
from db import db
from services.seed_service import seed

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/wwii_missions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

app.register_blueprint(mission_bp)




if __name__ == '__main__':
    app.run(debug=True)