from mongoengine import *
from datetime import datetime
from app.models.idea import Idea
from app.models.quick_memo import QuickMemo


class User(Document):
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


class ToDoLog(EmbeddedDocument):
    todo_create = IntField(required=True, default=0)
    milestone_complete = IntField(required=True, default=0)
    todo_complete = IntField(required=True, default=0)
    total = IntField(required=True, default=0)


class IdeasLog(EmbeddedDocument):
    vote = IntField(required=True, default=0)
    comment = IntField(required=True, default=0)
    idea_create = IntField(required=True, default=0)
    total = IntField(required=True, default=0)


class UserLog(Document):
    user = ReferenceField(document_type=User, required=True)
    date = DateTimeField(required=True, default=datetime.now())
    ToDo = EmbeddedDocumentField(document_type=ToDoLog, required=True, default=IdeasLog())
    Ideas = EmbeddedDocumentField(document_type=IdeasLog, required=True, default=IdeasLog())
