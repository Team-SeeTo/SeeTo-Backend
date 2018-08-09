from uuid import uuid4

import graphene
from flask_graphql_auth import create_access_token, create_refresh_token, get_jwt_identity

from app.schema.utils import blacklist, refresh_required
from app.models import User


class AuthMutation(graphene.Mutation):

    class Arguments(object):
        email = graphene.String()
        password = graphene.String()

    access_token = graphene.String()
    refresh_token = graphene.String()
    message = graphene.String()

    def mutate(self, info, **kwargs):
        user = User.objects(**kwargs).first()

        if user is not None:
            access_token = create_access_token(identity=kwargs["email"])
            refresh_token = create_refresh_token(identity=str(uuid4()))

            return AuthMutation(access_token=access_token, refresh_token=refresh_token, message="Login Success")
        else:
            return AuthMutation(message="Login failed")


class RefreshMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()

    access_token = graphene.String()
    message = graphene.String()

    @refresh_required
    def mutate(self, info):
        return RefreshMutation(acces_token=create_access_token(get_jwt_identity()), message="Refresh success")


class LogoutMutation(graphene.Mutation):

    class Arguments(object):
        token = graphene.String()

    is_success = graphene.Boolean()
    message = graphene.String()

    @refresh_required
    def mutate(self, info):
        blacklist.add(get_jwt_identity())
        return LogoutMutation(is_success=True, message="Logout successful")