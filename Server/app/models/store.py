from mongoengine import *
from extras_mongoengine.fields import IntEnumField
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
    effect = IntEnumField(Effect, default=Effect.FREEZE)
