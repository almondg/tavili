__author__ = 'Ronny'

from mongoengine import *
from models.all import *

from lib.mandrill_service import mandrill_serv


class Query:
  # check if there's a friend in the location of my new wish
  # pre - a new wish in the users list
  # returns - list of user_id of the friends in the new wish's location

  def __init__(self):
    self.mandrill_service = mandrill_serv

  def addToWishList(self, user, wish_item):
    user.wish_list.append(wish_item)
    user.save()

    relevantFriends = []
    for friend_id in user.friend_list:
      try:
        friend = User.objects(facebook_id=friend_id).get()
        if friend.current_location == wish_item.location or friend.address == wish_item.location:
          relevantFriends.append(friend)
      except:
        pass

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
    user.current_location = location
    user.save()

    relevantFriends = []
    for friend_id in user.friend_list:
      try:
        friend = User.objects(facebook_id=friend_id).get()
        for wish in friend.wish_list:
          if wish.location == location:
            relevantFriends.append({"friend": friend,
                                    "wish": wish})
            msg = "".join([user.name, " is in ", wish.location,
                           " and can fulfill your wish to have a ",
                           wish.product, ". Facebook him =)"])
            self.mandrill_service.send("friendshipping@gmail.com", friend.email,
                                       "Updates from FriendShipping App", msg)
      except:
        pass

    for friend_and_wish in relevantFriends:
      friend = friend_and_wish["friend"]
      wish = friend_and_wish["wish"]
      msg = "".join([friend.name, " wants a ", wish.product,
                     " from ", wish.location, ". Help him =)"])
      self.mandrill_service.send("friendshipping@gmail.com", user.email,
                                 "Updates from FriendShipping App", msg)

    return relevantFriends
