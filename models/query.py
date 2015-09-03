__author__ = 'Ronny'

import facebook
import requests
from models.all import *

class Query:
  # check if there's a friend in the location of my new wish
  # pre - a new wish in the users list
  # returns - list of user_id of the friends in the new wish's location

  def addToWishList(self, user, wish_item):
    relevantFriends = []
    for friend_id in user.friend_list:
      friend = User.objects(user_id=friend_id).get()
      if friend.location == wish_item.location:
        relevantFriends.append(friend.user_id)
        print (friend.user_id, "can get you a ", wish_item.product)

    token_app = ""
    if len(relevantFriends) > 0:
      graphAPI = facebook.GraphAPI(user.access_token)
      graphAPI.post(path="me/notifications",
                    template="You Have a New Friend Want to Fulfill Your Wish!",
                    href="http://intense-badlands-1277.herokuapp.com/",
                    access_token=token_app)
    return relevantFriends

  # check if there's a friend's wish in the location the user's traveling to
  # returns - list of user_id of the friends that needs something from the users' location

  def travelToLocation(self, user, location):
    relevantFriends = []
    for friend_id in user.friend_list:
      friend = User.objects(user_id=friend_id).get()
      for wish in friend.wishList:
        if wish.loaction == location:
          relevantFriends.append(friend.user_id)
          print(friend.user_id, "wants a ", wish.product)

    return relevantFriends
