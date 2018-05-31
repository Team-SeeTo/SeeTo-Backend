from mongoengine import *
from extras_mongoengine.fields import IntEnumField
from datetime import datetime
from enum import Enum


class TypeEnum(Enum):
    INFINITY = 1
    STANDARD = 2
    HARD = 3
    THREED = 4


class Milestone(Document):
    name = StringField(required=True)
    is_completed = BooleanField(required=True, default=False)


class ToDo(Document):
    meta = {'allow_inheritance': True,
            'collection': 'todo'}

    title = StringField(required=True)
    expiration = DateTimeField(required=True)
    type = IntEnumField(TypeEnum, required=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    point = IntField(required=True, default=10)


class ToDoStandard(ToDo):
    milestones = EmbeddedDocumentListField(Milestone, required=True)


class ToDo3Day(ToDo):
    day1 = EmbeddedDocumentListField(Milestone, required=True)
    day2 = EmbeddedDocumentListField(Milestone, required=True)
    day3 = EmbeddedDocumentListField(Milestone, required=True)
    last_refresh = DateTimeField(required=True, default=datetime.now())

