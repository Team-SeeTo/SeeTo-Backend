from mongoengine import *
from datetime import datetime
from .user import User


class Comment(EmbeddedDocument):
    author = ReferenceField(document_type=User, required=True)
    body = StringField(required=True)


class Idea(Document):
    meta = {'collection': 'idea'}

<<<<<<< HEAD
=======
    author = ReferenceField(document_type=User)
>>>>>>> 7194a8fb13c5de5d6fc1a208b14951d638f2ca60
    title = StringField(required=True)
    body = StringField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    point = IntField(required=True, default=10)
    upvoter = ListField(ReferenceField(document_type=User), required=True, default=[])
    comments = EmbeddedDocumentListField(Comment, default=[])
