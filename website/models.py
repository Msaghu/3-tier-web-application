#Create our database models for users & notes
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    #To show datetime
    #shows the relationship with the other model i.e class, user and primary key, id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#class Images(db.Model):
#define fields that we want to store

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=True)
    first_name = db.Column(db.String(150), nullable=True)
    #shows the relationship with thye other model, note
    notes = db.relationship('Note')