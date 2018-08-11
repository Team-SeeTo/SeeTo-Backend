from mongoengine import *
from datetime import datetime


class QuickMemo(Document):
    meta = {'collection': 'quick_memo'}

    title = StringField(required=True)
    body = StringField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now)
    point = IntField(required=True, default=10)
    tag = ListField(StringField, default=[])
