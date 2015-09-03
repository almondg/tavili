__author__ = 'Ronny'

class Query (){

    def getWishList (user):
        return user.wishList


    def travelToLocation (user,location):
        relevantFriends = []
        for friend in user.friendList:
            for wish in friend.wishList:
                if wish.location == location:
                    relevantFriends.append(friend.friend_id)

        return relevantFriends

}