# authentication_system_from_scratch
Authentication System

This is a simple Django project that demonstrates
how to implement basic authentication using function-based views.

Usage
Login

To access the login page, navigate to http://localhost:8000.

The login page contains a form where users can enter their username and password. 
There are two views that handle the login process: login and logout, both located in the shop/views.py file.

Login view

The login view is responsible for rendering the login form and handling form submissions. When the form is submitted, the view checks if the submitted credentials are valid and logs the user in if they are. If the credentials are invalid, an error message is displayed on the login page.
Logout view

The logout view is responsible for logging the user out and redirecting them to the login page.
