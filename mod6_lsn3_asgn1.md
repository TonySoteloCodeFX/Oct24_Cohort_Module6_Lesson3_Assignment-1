<h1>Module 6 Lesson 3:<br>Introduction to Object-relational Mappers (ORM)</h1>
<hr>

<h2>Flask-SQLAlchemy Fitness Center Management</h2>

<b>Objective:</b> The aim of this assignment is to transition from a traditional SQL approach to using Flask-SQLAlchemy for managing a fitness center's database. This assignment will enhance your skills in ORM (Object-Relational Mapping), specifically with Flask-SQLAlchemy, to build RESTful APIs for handling database operations with `Members` and `WorkoutSessions` tables.

<b><i>Task 1: Setting Up Flask with Flask-SQLAlchemy</i></b>

- Initialize a new Flask project and set up a virtual environment.
<br>
- Install Flask, Flask-SQLAlchemy, and Flask-Marshmallow.
<br>
- Configure Flask-SQLAlchemy to connect to your database.
<br>
- Define `Members` and `WorkoutSessions` models using Flask-SQLAlchemy ORM.

<b>Expected Outcome:</b> A Flask project connected to a database using SQLAlchemy with ORM models for `Members` and `WorkoutSessions`.

<b>Code Example:</b>

```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'
db = SQLAlchemy(app)

class Member(db.Model):
    # Define fields...

class WorkoutSession(db.Model):
    # Define fields...
```

<b><i>Task 2: Implementing CRUD Operations for Members Using ORM</i></b>

- Create Flask routes to add, retrieve, update, and delete members using the ORM models.
<br>
- Apply HTTP methods: POST to add, GET to retrieve, PUT to update, and DELETE to delete members.
<br>
- Handle errors effectively and return appropriate JSON responses.

<b>Expected Outcome:</b> Functional API endpoints for managing members in the database using Flask-SQLAlchemy, with proper error handling.

<b><i>Task 3: Managing Workout Sessions with ORM</i></b>

- Develop routes to schedule, update, and view workout sessions using SQLAlchemy.
<br>
- Implement a route to retrieve all workout sessions for a specific member.

<b>Expected Outcome:</b> A comprehensive set of endpoints for scheduling and viewing workout sessions using Flask-SQLAlchemy, with detailed information about each session.