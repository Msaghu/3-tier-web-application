To handle creation of templates
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
#from passlib.hash import sha256_crypt
from passlib.hash import pbkdf2_sha256

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()


        if user:
            #if password == user.password:
            if pbkdf2_sha256.verify(user.password, password):
                flash('Logged in successfully!', category='success')
            #if check_password_hash(user.password, password):
            #    login_user(user)
            #    flash('Logged in successfully!', category='success')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        #password1 = request.form.get('password1')
        #password2 = request.form.get('password2')
        password = sha256_crypt.encrypt("password")
        password2 = sha256_crypt.encrypt("password")

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
            #add user to the database password=generate_password_hash(password1, method='sha256') / password = generate_password_hash(password1, method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=email, first_name=first_name, password = pbkdf2_sha256.hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Account created successfully!', category='sucess')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
