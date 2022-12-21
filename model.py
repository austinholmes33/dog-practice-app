import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_trainer = db.Column(db.Boolean, default=False)
    datetime_created = db.Column(db.DateTime, default = datetime.now())

class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    breed = db.Column(db.String(200), nullable=False)
    color = db.Column(db.String(200), nullable=False)
    birthday = db.Column(db.DateTime, nullable=True)
    




def connect_to_db(app, db_uri=os.environ["DATABASE_URI"]):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.app = app
    db.init_app(app)
    print("Connected to dog db")

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)