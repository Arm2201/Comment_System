Welcome to my Comment System Project!

This is a Django-based web application for creating and managing comments on a webpage. 
It utilizes Django's form handling capabilities along with the crispy_forms package for styling the form elements. 
The project is structured using the standard Django application format.

Project Structure--->
The main directories and files in this project include:

comment_app: Contains the core application logic.
forms.py: Defines the form for creating comments.
models.py: Defines the database structure for storing comments.
views.py: Handles the request and response logic, rendering the form and processing user input.
page.html: The frontend template that displays the comment form.
settings.py: Configuration settings for the Django project.
urls.py: URL routing configuration.
db.sqlite3: Database file to store comment data.


Features:
Displays a comment form on the webpage using page.html.
Uses Django's CSRF protection for secure form submissions.
Leverages crispy_forms for better form styling and layout.
The form data is processed using views.py and saved to the database.


Prerequisites:
Python (version 3.x)
Django (version 5.1.4 as shown in the terminal)
django-crispy-forms package

Run the followiing commands:
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
