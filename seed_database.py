import os
from model import db, connect_to_db, User, Dog, Message, Post, Connect
from flask import Flask
from datetime import datetime

app = Flask(__name__)

connect_to_db(app)

# drop the existing db
os.system("dropdb dog-app")

# recreate the db
os.system("createdb dog-app")

# creates our tables
db.create_all()

# dummy users
user1 = User("hank", "hill", "propane@test.test", "test1")
user2 = User("peter", "griffin", "grindsgears@test.com", "test2")
user3 = User("bart", "simpson", "eatshorts@test.com", "test3")
trainer1 = User("cesar", "milan", "dogwhisper@test.com", "test4", is_trainer=True)
trainer2 = User("heather", "white", "heather@test.com", "test5", is_trainer=True)

# add dog owners and trainers
db.session.add_all([user1, user2, user3, trainer1, trainer2])
db.session.commit()

# dummy dogs

dog1 = Dog(1, "lady bird", "golden retriever", "gold", datetime(1982, 6, 1), "no steaks cooked with charcoal")
dog2 = Dog(2, "brian", "white dog", "white", datetime(1995, 9, 1), "vegan")
dog3 = Dog(3, "santas little helper", "greyhound", "brown", datetime(1989, 12, 24), "eats food")
dog4 = Dog(4, "kaya", "border collie", "white and black", datetime(2020, 10, 24), "dogfood")

# commit dogs to db

db.session.add_all([dog1, dog2, dog3, dog4])
db.session.commit()