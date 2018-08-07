from mongoengine import connect
from .idea import Idea, Comment
from .quick_memo import QuickMemo
from .todo import ToDo, Type, Milestone
from .user import User
from .store import StoreItem, Effect


class Mongo:

    def __init__(self, app):
        settings = app.config['MONGODB_SETTINGS']

        connect(**settings)

        print('[INFO] MongoEngine initialized with {}'.format(settings))
