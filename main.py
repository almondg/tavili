import sys
import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine

from lib.configure import configure_app
from controllers.general import ctrl as general_ctrl

from db.seed import seed_all

app = Flask(__name__, static_folder="public")
db = MongoEngine()
configure_app(app, db)

app.register_blueprint(general_ctrl)

if __name__ == "__main__":
  # Run the app.
  app.run()