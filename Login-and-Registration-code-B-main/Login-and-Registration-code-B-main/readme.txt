Project: loginpro - Django User Authentication Web Application

1. Project Overview:
This project is a Django-based web application named "loginpro" that provides user authentication functionality. It includes user registration, login, a protected dashboard page, and logout features. The application uses a single Django app called "loginapp".

2. Setup Instructions:
Requirements:
- Python (3.x recommended)
- Django 5.2
- SQLite (default database)

Setup Steps:
1. Create and activate a Python virtual environment:
   python3 -m venv venv
   source venv/bin/activate   (Linux/macOS)
   venv\Scripts\activate      (Windows)

2. Install Django:
   pip install django==5.2

3. Navigate to the project directory (where manage.py is located).

4. Run database migrations:
   python manage.py migrate

5. Start the development server:
   python manage.py runserver

6. Access the application in your browser at:
   http://127.0.0.1:8000/

3. Usage:
- Register a new user by visiting the root URL ("/") which shows the registration page.
- After successful registration, you will be redirected to the login page ("/login/").
- Login using your username or email and password.
- Upon successful login, you will be redirected to the dashboard page ("/dashboard/"), which is protected and requires authentication.
- Use the logout button on the dashboard to log out and return to the login page.

4. Project Structure:
- loginpro/: Django project configuration directory containing settings.py, urls.py, wsgi.py, and asgi.py.
- loginapp/: Django app containing views, forms, models, urls, and migrations.
- template/: Contains HTML templates for registration, login, and dashboard pages.
- manage.py: Django command-line utility for administrative tasks.
- db.sqlite3: SQLite database file (created after migrations).

URL Routing:
- "/" -> Registration page
- "/login/" -> Login page
- "/dashboard/" -> Dashboard page (login required)
- "/logout/" -> Logout and redirect to login

5. Technologies Used:
- Django 5.2: Web framework for Python.
- Bootstrap 5.3: CSS framework used for styling the HTML templates.
- SQLite: Default database used for storing user data.

This project provides a simple and clean user authentication system using Django's built-in User model and authentication framework, styled with Bootstrap for a responsive UI.
