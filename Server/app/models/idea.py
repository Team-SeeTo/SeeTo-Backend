from mongoengine import *
from datetime import datetime


class Comment(EmbeddedDocument):
    author = ObjectIdField(required=True)


class Idea(Document):
    meta = {'collection': 'idea'}

    title = StringField(required=True)
    body = StringField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    point = IntField(required=True, default=10)
    upvoters = ListField(ObjectIdField, required=True, default=[])
    comments = EmbeddedDocumentListField(Comment, default=[])
