from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sql_password import my_password

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{my_password}@127.0.0.1/fitness_center_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Members(db.Model):
    __members__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

class WorkoutSession(db.Model):
    __workout_sessions = 'workout_sessions'
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member_id'))
    session_date = db.Column(db.String, nullable=False)
    session_time = db.Column(db.String, nullable=False)
    session_duration_minutes = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)
