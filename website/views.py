#To show our html pages
from flask import Blueprint, render_template
from flask_login import current_user  # Import the current_user from Flask-Login
#In web applications, you often need to pass data from your application’s Python files to your HTML templates. To demonstrate how to do this in this application, you will pass a variable containing the current UTC date and time to the index template, and you’ll display the value of the variable in the template.

views = Blueprint('views', __name__)

@views.route('/')
def home():
    #Pass the user variable to the template context 
    return render_template("home.html", user=current_user)
