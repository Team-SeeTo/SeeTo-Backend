from mongoengine import *
from enum import Enum


class Effect(Enum):
    FREEZE = 0
    DOUBLE_TODO = 1
    DOUBLE_IDEAS = 2
    DOUBLE_24 = 3


class StoreItem(Document):
    meta = {'collection': 'store_item'}

    name = StringField(required=True)
    price = IntField(required=True)
    effect = StringField(required=True, default=Effect.FREEZE.name)
