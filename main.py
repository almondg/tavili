import sys
import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine

from lib.configure import configure_app

app = Flask(__name__, static_folder="public")
db = MongoEngine()
configure_app(app, db)

if __name__ == "__main__":
  # Run the app.
  app.run()