from mongoengine import *
from datetime import datetime
from app.models.idea import Idea
from app.models.quick_memo import QuickMemo


class UserModel(Document):
    meta = {'collection': 'user'}

    email = StringField(required=True, unique=True)
    username = StringField(required=True)
    password = StringField(required=True)
    rank = StringField(required=True)
    point = StringField(required=True, default=10)
    quick_memo = ListField(ReferenceField(QuickMemo), default=[])
    todo = ListField(GenericReferenceField, default=[])
    ideas = ListField(ReferenceField(Idea), default=[])
    register_on = DateTimeField(required=True, default=datetime.now())
