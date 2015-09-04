from flask import g
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import current_user
import os

from lib.mandrill_service import mandrill_serv

def configure_app(app, db, login_service=None):
  # Choose configuration environment.
  config_name = os.environ.get("SERVER_ENV", "development")
  print("Config Name: " + config_name)
  app.config.from_pyfile(
      os.path.join(os.getcwd() + "/config/" + ("%s.py" % config_name)))

  # Apply any changes from environment variable.
  app.config.from_envvar("SERVER_CONFIG", silent=True)

  # Configure database, and set the session to be stored in MongoDB.
  db.init_app(app)
  app.session_interface = MongoEngineSessionInterface(db)

  mandrill_serv.initialize(app.config)

  # Saves the user (Employee or User in our case) that requested something
  # from our server into global g of flask.
  @app.before_request
  def before_request():
    # Set up the Employee.
    g.login = current_user

    # Copy over config details.
    g.secret_key = app.config["SECRET_KEY"]

  # Configure the login service.
  # login_service.configure(app)
