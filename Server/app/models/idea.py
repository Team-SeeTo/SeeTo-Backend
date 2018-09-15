from mongoengine import *
from datetime import datetime
# from app.models import User


class Comment(EmbeddedDocument):
    author = GenericReferenceField(required=True)
    body = StringField(required=True)


class Idea(Document):
    meta = {'collection': 'idea'}

    author = GenericReferenceField(unique=True)
    title = StringField(required=True)
    body = StringField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now)
    point = IntField(required=True, default=10)
    upvoter = ListField(GenericReferenceField(), default=[])
    comments = EmbeddedDocumentListField(Comment, default=[])
    category = StringField(required=True)
