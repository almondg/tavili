__author__ = 'Ronny'

from facepy import GraphAPI
from models.all import *

from lib.mandrill_service import MandrillCommunicationService

class Query:
  # check if there's a friend in the location of my new wish
  # pre - a new wish in the users list
  # returns - list of user_id of the friends in the new wish's location

  def __init__(self):
    self.mandrill_service = MandrillCommunicationService()
    self.mandrill_service.initialize()


  def addToWishList(self, user, wish_item):
    relevantFriends = []
    for friend_id in user.friend_list:
      friend = User.objects(user_id=friend_id).get()
      if friend.location == wish_item.location:
        relevantFriends.append(friend.user_id)
        print (friend.user_id, "can get you a ", wish_item.product)

    if len(relevantFriends) > 0:
      self.mandrill_service.send("friendshipping@gmail.com", user.email, "Updates from FriendShipping App",
                                 "You have a new friend want to fulfill your wish. Enter the app and connect your friend.")
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
          self.mandrill_service.send("friendshipping@gmail.com", friend.email, "Updates from FriendShipping App",
                                 "You have a new friend want to fulfill your wish. Enter the app and connect your friend.")

    if len(relevantFriends) > 0:
      self.mandrill_service.send("friendshipping@gmail.com", user.email, "Updates from FriendShipping App",
                                 "You have a new friend you can help to fulfill his wish. Enter the app and connect your friend.")

    return relevantFriends
