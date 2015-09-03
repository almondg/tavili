__author__ = 'shaked'

from flask import Flask
from flask.ext.mongoengine import MongoEngine

from lib.configure import configure_app
from models.all import *

def seed_users():
  User.drop_collection()

  wishItem1 = WishItem(location="Germany", product="iPhone 5")
  wishItem2 = WishItem(location="USA", product="iPhone 6S")

  user1 = User(facebook_id="1234", current_location="New York", address="Rothschild 22",
               friend_list=["U123456789123456", "U123456789000000", "U123456789111111"])
  user1.wish_list.append(wishItem1)
  user1.wish_list.append(wishItem2)

  user1.save()

def seed_all():
  seed_users()


if __name__ == "__main__":
  # Create and initialize the app.
  app = Flask(__name__, static_folder="public")
  db = MongoEngine()
  configure_app(app, db)

  # Seed the DB.
  seed_all()
