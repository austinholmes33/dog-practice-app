import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

###### MODELS ######

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_trainer = db.Column(db.Boolean, default=False)
    datetime_created = db.Column(db.DateTime, default = datetime.now())

    def __init__(self, first_name, last_name, email, password, is_trainer=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_trainer = is_trainer
    
    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    breed = db.Column(db.String(200), nullable=False)
    color = db.Column(db.String(200), nullable=False)
    birthday = db.Column(db.DateTime, nullable=True)
    dietary_info = db.Column(db.String(length=999), nullable=True)
    datetime_created = db.Column(db.Datetime, default=datetime.now())

    def __init__(self, user_id, name, breed, color, birthday, dietary_info):
        self.user_id = user_id
        self.name = name
        self.breed = breed
        self.color = color
        self.birthday = birthday
        self.dietary_info = dietary_info

    def __repr__(self):
        return f"<Dog {self.name}>"

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dog_id = db.Column(db.Integer, db.ForeignKey("dogs.id"), nullable=False)
    from_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    to_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    datetime_created = db.Column(db.Datetime, default=datetime.now())

    def __init__(self, dog_id, from_user_id, to_user_id, content):
        self.dog_id = dog_id
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.content = content

    def __repr__(self):
        f"<Message {self.content}>"

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    datetime_created = db.Column(db.Datetime, default=datetime.now())

    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        f"<Post {self.content}>"

class Connect(db.Model):
    __tablename__ = "connects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    connector_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    connectee_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, connector_id, conntectee_id):
        self.connector_id = connector_id
        self.connectee_id = conntectee_id


####### CONNECT FLASK APP TO SQLALCHEMY APP #######

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