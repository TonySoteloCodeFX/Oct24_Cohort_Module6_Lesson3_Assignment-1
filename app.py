from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sql_password import my_password
from marshmallow import fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{my_password}@127.0.0.1/fitness_center_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    workouts = db.relationship('WorkoutSession', backref='member')

class WorkoutSession(db.Model):
    __tablename__ = 'workout_sessions'
    id = db.Column(db.Integer, primary_key=True)
    session_date = db.Column(db.String, nullable=False)
    session_time = db.Column(db.String, nullable=False)
    session_duration_minutes = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))

# Schemas
class MemberSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    age = fields.Integer(required=True)

    class Meta:
        fields = ("id", "name", "age")

class WorkoutSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    member_id = fields.Integer(required=True)
    session_date = fields.String(required=True)
    session_time = fields.String(required=True)
    session_duration_minutes = fields.Integer(required=True)
    calories_burned = fields.Integer(required=True)

    class Meta:
        fields = ("id", "member_id", "session_date", "session_time", "session_duration_minutes", "calories_burned")

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

# Member Routes 
@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify(members_schema.dump(members)), 200

@app.route('/members', methods=['POST'])
def add_member():
    try:
        member_data = member_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    new_member = Member(name=member_data['name'], age=member_data['age'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'Message': 'New member added successfully.'}), 201

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    member = Member.query.get_or_404(id)
    try:
        member_data = member_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    member.name = member_data['name']
    member.age = member_data['age']
    db.session.commit()
    return jsonify({'Message': 'Member details updated successfully'}), 200

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({'Message': 'Member deleted successfully.'}), 200

# Workout Routes 
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = WorkoutSession.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200

@app.route('/workouts/member/<int:member_id>', methods=['GET'])
def get_workouts_by_member_id(member_id):
    workouts = WorkoutSession.query.filter_by(member_id=member_id).all()
    return jsonify(workouts_schema.dump(workouts)), 200

@app.route('/workouts', methods=['POST'])
def add_workout():
    try:
        workout_data = workout_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    new_workout = WorkoutSession(
        session_date=workout_data['session_date'],
        session_time=workout_data['session_time'],
        session_duration_minutes=workout_data['session_duration_minutes'],
        calories_burned=workout_data['calories_burned'],
        member_id=workout_data['member_id'])
    db.session.add(new_workout)
    db.session.commit()
    return jsonify({'Message': 'New Workout Session added successfully.'}), 201

@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    workout = WorkoutSession.query.get_or_404(id)
    try:
        workout_data = workout_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    workout.member_id = workout_data['member_id']
    workout.session_date = workout_data['session_date']
    workout.session_time = workout_data['session_time']
    workout.session_duration_minutes = workout_data['session_duration_minutes']
    workout.calories_burned = workout_data['calories_burned']
    db.session.commit()
    return jsonify({'Message': 'Workout details updated successfully'}), 200

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = WorkoutSession.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify({'Message': 'Workout deleted successfully.'}), 200

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
