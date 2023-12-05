#To handle creation of templates
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from passlib.hash import pbkdf2_sha256
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password_entered = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        #Verifying credentials
        if user:
            if pbkdf2_sha256.verify(password_entered, user.password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        hashed_password = pbkdf2_sha256.hash(password1)

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists!', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords dont match!', category='error')
        elif len(password1) < 7:
            flash('Password cannot be less than 7 characters.', category='error')
        elif not password1[0].isupper():
            flash("Password must start with a capital letter.")
        elif not any(char.isdigit() for char in password1):
            flash("Password must contain at least one digit.")
        else:
            #add user to the database 
            
            new_user = User(email=email, first_name=first_name, password = hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created successfully!', category='sucess')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
