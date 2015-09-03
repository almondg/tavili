__author__ = 'shaked'

import itertools

from dateutil.parser import parse
from flask import Blueprint, jsonify, request, g
from mongoengine import Q

class GeneralController(Blueprint):

    def getUserInfo(self):
      """
      Returns the User info for the currently logged in User.
      If the User is active, the list of Debts are returned as well.
      """
      user = g.user
      if not user:
        return None

      return user.toFullJson()

ctrl = GeneralController("general", __name__, static_folder="../public")

# Signal handlers.
# @login_service.new_session.connect_via(login_service)
# def handle_new_session(login_service, login, role, **extras):
#   if role == Login.Role.USER:
#     ctrl.createNewWebCommunication(login.user, request.args.get("ref"))

# User API paths.
@ctrl.route("/api/user/info/")
def get_user_info():
  info = ctrl.getUserInfo()
  if not info:
    return jsonify(err=("No user found for ID: '%s'" % g.user.user_id))
  return jsonify(info=info)