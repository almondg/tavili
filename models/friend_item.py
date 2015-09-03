__author__ = 'Ronny'

from mongoengine import *

from lib.id_generator import randomIdGenerator


class FriendItem(EmbeddedDocument):

  item_id = StringField(default=randomIdGenerator("WI"))

  location = StringField()

  address = StringField()


  def toMinimalJson(self):
    return {
      "itemId": self.item_id,
      "location": self.location,
      "address": self.address,
    }

  def toFullJson(self):
    return self.toMinimalJson()