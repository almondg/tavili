__author__ = 'Ronny'

class Query (){
    # check if there's a friend in the location of my new wish
    # pre - a new wish in the users list
    # returns - list of user_id of the friends in the new wish's location

    def addToWishList(user,WishItem):
        relevantFriends = []
        for friend in user.friendList:
            if friend.location == WishItem.location:
                relevantFriends.append(friend.user_id)




    # check if there's a friend's wish in the location the user's traveling to
    # returns - list of user_id of the friends that needs something from the users' location

    def travelToLocation (user,location):
        relevantFriends = []
        for friend in user.friendList:
            for wish in friend.wishList:
                if wish.loaction == location:
                    relevantFriends.append(friend.user_id)

        return relevantFriends
}