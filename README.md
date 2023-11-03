# Flask-Firebase Task Manager API

A simple RESTful API for managing tasks built with Flask and Firebase Firestore.

## Features

- Create, Retrieve, Update, and Delete tasks
- Data validation
- Error handling

## Installation

Before starting, make sure you have Python 3.9+ installed on your system. Then, follow these steps to get the API up and running:

### Clone the repository

```bash
git clone https://github.com/yourusername/flask-firebase-task-api.git
cd flask-firebase-task-api
```

Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
```

Install dependencies
```bash
pip install -r requirements.txt
```

Start the server
```bash
flask run
```

The API should now be accessible at http://127.0.0.1:5000/.

### Usage
## The API endpoints include:

- **GET /api/v1/tasks**: Get all tasks.
- **POST /api/v1/tasks**: Create a new task. Request body should include title, description, and optionally status.
- **GET /api/v1/tasks/:id**: Get details of a specific task.
- **PATCH /api/v1/tasks/:id**: Update a task with a given ID. Request body may include title, description, and status.
- **DELETE /api/v1/tasks/:id**: Delete a task with a given ID.# todo-list-api
