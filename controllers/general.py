__author__ = 'shaked'

from flask import Blueprint, jsonify, request, g

from models.all import *


class GeneralController(Blueprint):

  def getUserInfo(self):
    """
    Returns the User info for the currently logged in User.
    If the User is active, the list of Debts are returned as well.
    """
    users = User.objects().all()

    return [user.toMinimalJson() for user in users]

  def handleFacebookLogin(self, facebook_id, name, location, address, friends_list, access_token, email):
    q = Query()
    try:
      user = User.objects(facebook_id=facebook_id).get()
      if user:
        user.current_location = location
        user.address = address
        user.friend_list = friends_list
        user.access_token = access_token
        user.email = email
        user.save()
      q.travelToLocation(user, location)
    except:
      user = User(facebook_id=facebook_id, name=name, current_location=location,
                  address=address, friend_list=friends_list, access_token=access_token,
                  email=email)
      user.save()
      q.travelToLocation(user, location)

    return "Successfully Logged In."

  def getUserWishList(self, facebook_id):
    try:
      user = User.objects(facebook_id=facebook_id).get()
      return user.wish_list
    except:
      return None

  def handleAddToWishList(self, facebook_id, location, product):
    try:
      user = User.objects(facebook_id=facebook_id).get()
      q = Query()
      q.addToWishList(user, WishItem(location=location, product=product))
      return self.getUserWishList(facebook_id)
    except:
      return None

  def handleRemoveFromWishList(self, facebook_id, item_id):
    try:
      user = User.objects(facebook_id=facebook_id).get()
      q = Query()
      q.removeFromWishList(user, item_id)
      return self.getUserWishList(facebook_id)
    except:
      return None


ctrl = GeneralController("general", __name__, static_folder="../public")

@ctrl.route("/")
def user_path():
  return ctrl.send_static_file("app/index.html")


@ctrl.route("/api/user/info/")
def get_user_info():
  info = ctrl.getUserInfo()
  if not info:
    return jsonify(err=("No user found for ID: '%s'" % g.user.user_id))
  return jsonify(info=info)


@ctrl.route("/api/user/login/", methods=["POST"])
def login_user():
  facebook_id = request.form.get("userId")
  name = request.form.get("name")
  location = request.form.get("country")
  address = request.form.get("address")
  friends_list = request.form.get("friendIds")
  email = request.form.get("email")

  if not isinstance(friends_list, list) and friends_list:
    friends_list = friends_list.split(",")

  result = ctrl.handleFacebookLogin(facebook_id, name, location, address, friends_list, None, email)
  return jsonify(result=result)


@ctrl.route("/api/add_to_wishlist/", methods=["POST"])
def add_to_wishlist():
  product = request.form.get("product")
  location = request.form.get("location")
  facebook_id = request.form.get("fb_id")
  result = ctrl.handleAddToWishList(facebook_id, location, product)
  return jsonify(result=result)

@ctrl.route("/api/remove_from_wishlist/", methods=["POST"])
def remove_from_wishlist():
  item_id = request.form.get("item_id")
  facebook_id = request.form.get("fb_id")
  result = ctrl.handleRemoveFromWishList(facebook_id, item_id)
  return jsonify(result=result)

@ctrl.route("/api/get_wishlist/<fb_id>/")
def get_to_wishlist(fb_id):
  result = ctrl.getUserWishList(fb_id)
  return jsonify(result=result)
