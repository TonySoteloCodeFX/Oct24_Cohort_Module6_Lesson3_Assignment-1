<h1>Module 6 Lesson 3: Introduction to Object-relational Mappers (ORM)</h1>
<hr>

<h2>Main Module</h2>

- <b>app.py</b>
  - Serves as the main program

<h2>Models</h2>

- <b>Member()</b> - Holds column name and attributes for members table
<br>

- <b>WorkoutSession</b> - Holds column name and attributes for workout table

<h2>Schemas</h2>

- <b>MembersSchema()</b> - Holds fields to create member routes
<br>

- <b>WorkoutSchema()</b> - Holds fields to create workout routes 

<h2>Member Routes</h2>

- <b>get_members():</b> - Method 'GET'
  - Displays all members from Members Table
<br>

- <b>add_member()</b> - Method 'POST'
  - Adds a member to members table
<br>

- <b>update_member()</b> - Method 'PUT'
  - Updates the values from a member by member ID
<br>

- <b>delete_member()</b> - Method 'DELETE'
  - Deletes a member from members table by member ID
<br>

<h2>Workout Routes</h2>

- <b>get_workouts()</b> - Method 'GET'
  - Displays all workouts from workout table
<br>

- <b>get_workouts_by_member_id()</b> - Method 'GET'
  - Displays all workouts from a member by member ID
<br>

- <b>schedule_workout()</b> - Method 'POST'
  - Schedules a new workout into workout table by member ID
<br>

- <b>update_workout()</b> - Method 'PUT'
  - Updates a workout from workout table by workout ID
<br>

- <b>delete_workout()</b> - Method 'DELETE'
  - Deletes a workout by workout ID