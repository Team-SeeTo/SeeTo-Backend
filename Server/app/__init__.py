from flask import Flask
from app.schema import Schema
from flask_graphql_auth import GraphQLAuth

from app.schema.fields import ResponseMessageField
from app.models import User, Mongo


def create_app(*config_cls):
    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    print('[INFO] Flask application initialized with {}'.format([config.__name__ for config in config_cls]))

    GraphQLAuth().init_app(app_)
    Schema().init_app(app_)
    Mongo(app_)

    return app_