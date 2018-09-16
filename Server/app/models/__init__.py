from mongoengine import connect
from .quick_memo import QuickMemo
from .todo import ToDo, Type, Milestone
from .store import StoreItem, Effect
from .idea import Idea, Comment
from .user import User, UserLog, IdeasLog, ToDoLog


class Mongo:

    def __init__(self, app):
        settings = app.config['MONGODB_SETTINGS']

        connect(**settings)

        print('[INFO] MongoEngine initialized with {}'.format(settings))
