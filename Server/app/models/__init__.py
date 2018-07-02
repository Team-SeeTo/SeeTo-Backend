from mongoengine import connect
from .idea import Idea, Comment
from .quick_memo import QuickMemo
from .todo import ToDoStandard, ToDo, TypeEnum, Milestone
from .user import User

class Mongo:

    def __init__(self, app):
        settings = app.config['MONGODB_SETTINGS']

        connect(**settings)

        print('[INFO] MongoEngine initialized with {}'.format(settings))
