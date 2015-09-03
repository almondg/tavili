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
        relevantFriends.append(friend)

    for friend in relevantFriends:
      msg = "".join([friend.name, " is in ", wish_item.location,
                     " and can fulfill your wish to have a ",
                    wish_item.product, ". Facebook him =)"])
      self.mandrill_service.send("friendshipping@gmail.com", user.email,
                                 "Updates from FriendShipping App", msg)
    return relevantFriends

  # check if there's a friend's wish in the location the user's traveling to
  # returns - list of user_id of the friends that needs something from the users' location

  def travelToLocation(self, user, location):
    relevantFriends = []
    for friend_id in user.friend_list:
      friend = User.objects(user_id=friend_id).get()
      for wish in friend.wishList:
        if wish.loaction == location:
          relevantFriends.append({"friend": friend,
                                  "wish": wish})
          msg = "".join([friend.name, " is in ", wish.location,
                        " and can fulfill your wish to have a ",
                        wish.product, ". Facebook him =)"])
          self.mandrill_service.send("friendshipping@gmail.com", friend.email,
                                     "Updates from FriendShipping App", msg)

    for friend_and_wish in relevantFriends:
      friend = friend_and_wish["friend"]
      wish = friend_and_wish["wish"]
      msg = "".join([friend.name, " wants a ", wish.product,
                     " from ", wish.location, ". Help him =)"])
      self.mandrill_service.send("friendshipping@gmail.com", user.email,
                                 "Updates from FriendShipping App", msg)

    return relevantFriends
