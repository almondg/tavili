__author__ = 'shaked'

from mongoengine import *
from lib.id_generator import randomIdGenerator
from wish_item import WishItem

class User(Document):

  user_id = StringField(default=randomIdGenerator("U"))
  facebook_id = StringField() #/will get from login
  current_location = StringField() #/will get from login
  address = StringField() #/will get from login
  wish_list = ListField(EmbeddedDocumentField(WishItem))
  friend_list = ListField() #/will get from login
  access_token = StringField()

  def toMinimalJson(self):
    return {
      "userId": self.user_id,
      "facebookId" : self.facebook_id,
      "location" : self.current_location,
      "address" : self.address,
      "wishList": [item.toMinimalJson() for item in self.wish_list],
      "friendList": [item for item in self.friend_list],
    }

  def toFullJson(self):
    return self.toMinimalJson()

  def addToList(self,item):
    self.wish_list.append(item)

  def removeFromList(self,item):
      if item in self.wish_list:
        self.wish_list.remove(item)

