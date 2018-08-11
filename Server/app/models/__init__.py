from mongoengine import connect
from app.models.activity.todo import ToDo, Type, Milestone
from app.models.activity.idea import Idea, Comment
from app.models.activity.quick_memo import QuickMemo
from app.models.store.store import StoreItem, Effect
from app.models.user.user import User


class Mongo:

    def __init__(self, app):
        settings = app.config['MONGODB_SETTINGS']

        connect(**settings)

        print('[INFO] MongoEngine initialized with {}'.format(settings))
