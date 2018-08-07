from mongoengine import *
from extras_mongoengine.fields import IntEnumField
from datetime import datetime
from enum import Enum


class Type(Enum):
    INFINITY = 1
    STANDARD = 2
    HARD = 3


class Milestone(Document):
    name = StringField(required=True)
    is_completed = BooleanField(required=True, default=False)


class ToDo(Document):
    meta = {'collection': 'todo'}

    title = StringField(required=True)
    type = IntEnumField(Type, required=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    point = IntField(required=True, default=10)
    is_completed = BooleanField(required=True, default=False)
    milestones = EmbeddedDocumentListField(Milestone, required=True)
    expiration = DateTimeField(required=True)
