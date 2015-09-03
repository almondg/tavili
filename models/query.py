__author__ = 'Ronny'

from models.all import *

class Query:
  # check if there's a friend in the location of my new wish
  # pre - a new wish in the users list
  # returns - list of user_id of the friends in the new wish's location

  def addToWishList(user, wish_item):
    relevantFriends = []
    for friend_id in user.friend_list:
      friend = User.objects(user_id=friend_id).get()
      if friend.location == wish_item.location:
        relevantFriends.append(friend.user_id)
        print (friend.user_id, "can get you a ", wish_item.product)

    return relevantFriends

  # check if there's a friend's wish in the location the user's traveling to
  # returns - list of user_id of the friends that needs something from the users' location

  def travelToLocation(user, location):
    relevantFriends = []
    for friend_id in user.friend_list:
      friend = User.objects(user_id=friend_id).get()
      for wish in friend.wishList:
        if wish.loaction == location:
          relevantFriends.append(friend.user_id)
          print(friend.user_id, "wants a ", wish.product)

    return relevantFriends
