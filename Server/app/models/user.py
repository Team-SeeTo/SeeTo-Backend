from mongoengine import *
from datetime import datetime
from app.models import QuickMemo, StoreItem, ToDo, Idea


class User(Document):
    meta = {'collection': 'user'}

    email = StringField(primary_key=True)
    username = StringField(required=True)
    password = StringField(required=True)
    point = IntField(required=True, default=10)
    quick_memo = ListField(ReferenceField(QuickMemo), default=[])
    todo = ListField(ReferenceField(ToDo), default=[])
    ideas = ListField(ReferenceField(Idea), default=[])
    my_items = ListField(ReferenceField(StoreItem), default=[])
    register_on = DateTimeField(required=True, default=datetime.now)


class ToDoLog(EmbeddedDocument):
    new_create = IntField(required=True, default=0)
    milestone_complete = IntField(required=True, default=0)
    todo_complete = IntField(required=True, default=0)
    total_point = IntField(required=True, default=0)


class IdeasLog(EmbeddedDocument):
    new_vote = IntField(required=True, default=0)
    new_comment = IntField(required=True, default=0)
    new_create = IntField(required=True, default=0)
    total_point = IntField(required=True, default=0)


class UserLog(Document):
    user = ReferenceField(document_type=User, required=True)
    date = DateTimeField(required=True)
    todo = EmbeddedDocumentField(document_type=ToDoLog, required=True, default=ToDoLog)
    idea = EmbeddedDocumentField(document_type=IdeasLog, required=True, default=IdeasLog)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.now().date()
        return super(UserLog, self).save(*args, **kwargs)
