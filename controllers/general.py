__author__ = 'shaked'

import itertools

from dateutil.parser import parse
from flask import Blueprint, jsonify, request, g
from mongoengine import Q
import os

from models.all import *

class GeneralController(Blueprint):

    def getUserInfo(self):
      """
      Returns the User info for the currently logged in User.
      If the User is active, the list of Debts are returned as well.
      """
      users = User.objects().all()

      return [user.toMinimalJson() for user in users]

ctrl = GeneralController("general", __name__, static_folder="../public")

# Signal handlers.
# @login_service.new_session.connect_via(login_service)
# def handle_new_session(login_service, login, role, **extras):
#   if role == Login.Role.USER:
#     ctrl.createNewWebCommunication(login.user, request.args.get("ref"))

@ctrl.route("/")
def user_path():
    return ctrl.send_static_file(os.path.join("app", "index.html"))

@ctrl.route("/login")
def login_path():
    return ctrl.send_static_file(os.path.join("app", "Login.html"))

@ctrl.route("/home")
def home_path():
    return ctrl.send_static_file(os.path.join("app", "Home.html"))


@ctrl.route("/api/user/info/")
def get_user_info():
  info = ctrl.getUserInfo()
  if not info:
    return jsonify(err=("No user found for ID: '%s'" % g.user.user_id))
  return jsonify(info=info)