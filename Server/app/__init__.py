from functools import wraps
from flask import Flask
from app.schema import Schema
from flask_graphql_auth import GraphQLAuth

from app.schema.fields import ResponseMessageField
from flask_graphql_auth import jwt_required, get_jwt_identity, jwt_refresh_token_required
from app.models import User

blacklist = set()


def create_app(*config_cls):
    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    print('[INFO] Flask application initialized with {}'.format([config.__name__ for config in config_cls]))

    GraphQLAuth().init_app(app_)
    Schema().init_app(app_)

    return app_


def auth_required(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        account = User.objects(username=get_jwt_identity()).first()
        if account is None:
            return ResponseMessageField(is_success=False, message="Invalid access token")
        return fn(*args, **kwargs)
    return wrapper


def refresh_required(fn):
    @wraps(fn)
    @jwt_refresh_token_required
    def wrapper(*args, **kwargs):
        if get_jwt_identity() in blacklist:
            return ResponseMessageField(is_success=False, message="Invalid refresh token")
        else:
            return fn(*args, **kwargs)
    return wrapper
