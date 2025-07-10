Instructions here.
# Project Management API (Django)

## Features:
- User Registration/Login (JWT)
- Project, Task, Comment, Project Member Management
- API Documentation via Swagger

## Setup:
```bash
git clone <repo_url>
cd project_management
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py startapp api
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
