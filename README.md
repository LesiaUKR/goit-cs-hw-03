# Homework for the "Introduction to Database Management Systems" module

### Today you will:

- Create a database for a task management system using PostgreSQL and execute the required queries in the task management database.
- Develop a Python script that uses the PyMongo library to perform basic CRUD operations in MongoDB.

These tasks will help you strengthen your understanding of SQL and its interactions with relational databases, including data retrieval, updates, insertions, and analysis. By completing this homework, you’ll also learn how to use PyMongo methods to interact with a MongoDB cloud server from a Python script.

## Task Descriptions

## Task 1:

Create a database for a task management system using PostgreSQL. The database should include tables for users, task statuses, and tasks. Execute the required queries in the task management database.

### Step-by-Step Instructions:

1. Create tables in your PostgreSQL database based on the requirements. Use appropriate data types and constraints.

#### Database Structure Requirements:

**Table: users**

- id: Primary key, auto-increment (SERIAL type),
- fullname: User’s full name (VARCHAR(100) type),
- email: User’s email address, must be unique (VARCHAR(100) type).

**Table: status**

- id: Primary key, auto-increment (SERIAL type),
- name: Status name (VARCHAR(50) type), must be unique. Suggested
  statuses: ('new', 'in progress', 'completed').

**Table: tasks**

- id: Primary key, auto-increment (SERIAL type),
- title: Task title (VARCHAR(100) type),
- description: Task description (TEXT type),
- status_id: Foreign key referencing id in the status table (INTEGER type),
- user_id: Foreign key referencing id in the users table (INTEGER type).

![ER Diagram](assets/er_diagram.png)

2. Ensure that the email field in the users table and the name field in the status table are unique.

3. Set up relationships between tables so that deleting a user automatically deletes all their tasks (cascade deletion).

4. Write a script to create these tables.

5. Write a Python script (seed.py) to populate these tables with random data using the Faker library.

6. Using SQL, perform the following queries in the task management database:

**Required Queries:**

1. Retrieve all tasks for a specific user using their user_id.
2. Retrieve tasks with a specific status. Use a subquery to select tasks with a status like 'new'.
3. Update the status of a specific task to 'in progress' or another status.
4. Retrieve a list of users who have no tasks. Use a combination of SELECT, WHERE NOT IN, and a subquery.
5. Add a new task for a specific user using INSERT.
6. Retrieve all tasks that are not completed. Select tasks whose status is not 'completed'.
7. Delete a specific task using DELETE by its id.
8. Find users with a specific email address. Use SELECT with a LIKE condition to filter by email.
9. Update a user’s name using UPDATE.
10. Get the number of tasks for each status. Use SELECT, COUNT, and GROUP BY to group tasks by status.
11. Retrieve tasks assigned to users with a specific email domain. Use SELECT with a LIKE condition and JOIN to select tasks assigned to users with emails like %@example.com.
12. Retrieve tasks without a description. Select tasks where the description is NULL.
13. Select users and their tasks with a status of 'in progress'. Use INNER JOIN to get a list of users and their tasks with a specific status.
14. Get users and the count of their tasks. Use LEFT JOIN and GROUP BY to select users and count their tasks.

#### Acceptance Criteria:

1. Tables are created, and the database structure requirements are met.
2. The email field in the users table and the name field in the status table are unique.
3. Cascade deletion is configured to remove tasks when a user is deleted.
4. A script is provided for table creation.
5. A seed.py script populates the tables with random data using the Faker library.
6. All required queries are executed in the task management database.

## Task 2:

Develop a Python script that uses the PyMongo library to perform basic CRUD (Create, Read, Update, Delete) operations in MongoDB.

### Step-by-Step Instructions:

1. Create a database based on the requirements.

#### Document Structure Requirements:

Each document in your database should have the following structure:

```json
{
"_id": ObjectId("60d24b783733b1ae668d4a77"),
"name": "barsik",
"age": 3,
"features": ["walks in slippers", "allows petting", "ginger"]
}
```

This document represents information about a cat, including its name, age, and features.

2. Develop a Python script (main.py) to perform the following tasks:

#### Tasks to Perform:

**Read:**

- Implement a function to display all records in the collection.
- Implement a function that allows the user to input a cat's name and displays information about that cat.

**Update:**

- Create a function to allow the user to update a cat's age by name.
- Create a function to add a new feature to a cat's features list by name.

**Delete:**

- Implement a function to delete a record from the collection by the animal's name.
- Implement a function to delete all records from the collection.

💡 **Tips for Completion:**

- Use MongoDB Atlas or a locally installed MongoDB instance via Docker.
- Install the PyMongo library using pip, pipenv, or poetry.
- Handle potential exceptions when performing database operations.
- Ensure your functions are clearly commented and well-structured.
- Using Python virtual environments for project dependency isolation is encouraged.

#### Acceptance Criteria:

1. A database is created, and the document structure requirements are met.
2. All required operations are implemented.
3. Potential exceptions are handled during database operations.
4. Functions are clearly commented and well-structured.
