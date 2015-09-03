__author__ = 'shaked'

from mongoengine import *

from lib.id_generator import randomIdGenerator
from stringfield import StringField

class WishItem(EmbeddedDocument):

  item_id = StringField(default=randomIdGenerator("WI"))

  location = StringField()

  product = StringField()


  def toMinimalJson(self):
    return {
      "itemId": self.item_id,
      "location": self.location,
      "product": self.product,
    }

  def toFullJson(self):
    return self.toMinimalJson()