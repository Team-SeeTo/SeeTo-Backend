from mongoengine import *


class StoreItem(Document):
    meta = {'collection': 'store_item'}

    name = StringField(required=True)
    price = IntField(required=True)
    effect = StringField(required=True)
