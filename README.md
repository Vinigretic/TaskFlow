# Task Manager

Task Manager is a web application built on Python 3.11 and Django v4.2 that helps you manage tasks and projects effectively. It provides a simple interface for creating, updating and prioritizing tasks in projects, as well as setting deadlines and marking tasks as completed.
## Features

- Create, update, and delete projects
- Add, update, and delete tasks within projects
- Prioritize tasks within projects
- Set deadlines for tasks
- Mark tasks as 'done'
- User authentication and authorization with django-allauth
- Responsive design for desktop and mobile devices using Bootstrap v5

## Installation

```bash
1. Clone the repository:
https://github.com/Vinigretic/TaskFlow

2. Install dependencies:
pip install -r requirements.txt

3. Apply database migrations:
python manage.py migrate

4. Run the development server:
python manage.py runserver

5. Access the application in your web browser at http://localhost:8000.

Usage
Sign up for an account or log in if you already have one.
Create projects by clicking on the "Add TODO List" button.
Add tasks to your projects by clicking on the "Add Task".
Prioritize tasks by clicking on the task and selecting a priority.
Set deadlines for tasks by clicking on the task and selecting a date.
Mark tasks as 'done' by clicking on the checkbox next to the task.
Update or delete projects and tasks as needed.

Testing
To run automated tests, use the following command:
pytest






