__author__ = 'shaked'

from mongoengine import *

from lib.id_generator import randomIdGenerator
from wish_item import WishItem

class User(Document):

  user_id = StringField(default=randomIdGenerator("U"))

  wishlist = ListField(EmbeddedDocumentField(WishItem))


  def toMinimalJson(self):
    return {
      "userId": self.user_id,
      "wishlist": [item.toMinimalJson() for item in self.wishlist],
    }

  def toFullJson(self):
    return self.toMinimalJson()