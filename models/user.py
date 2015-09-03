__author__ = 'shaked'

from mongoengine import *
from lib.id_generator import randomIdGenerator
from wish_item import WishItem
from stringfield import StringField
from djangotoolbox.fields import EmbeddedDocumentField, ListField

class User(Document):

  user_id = StringField(default=randomIdGenerator("U"))
  fb_id = StringField()
  wishList = ListField(EmbeddedDocumentField(WishItem))
  friendList = ListField(EmbeddedDocumentField(FriendItem))


  def toMinimalJson(self):
    return {
      "userId": self.user_id,
      "FacebookId" : self.fb_id,
      "wishList": [item.toMinimalJson() for item in self.wishList],
      "friendList": [item.toMinimalJson() for item in self.friendList]
    }

  def toFullJson(self):
    return self.toMinimalJson()

  def addToList(self,item):
    self.wishList.insert(item)

  def removeFromList(self,item):
      if item in self.wishList:
        self.wishList.remove(item)

