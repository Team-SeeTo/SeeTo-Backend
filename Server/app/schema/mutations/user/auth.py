from uuid import uuid4

import graphene
from flask_graphql_auth import create_access_token, create_refresh_token,\
    get_jwt_identity, mutation_jwt_refresh_token_required

from app.models import User
from app.schema.fields import AuthField, RefreshField ,ResponseMessageField
from app.schema.unions import AuthUnion, RefreshUnion, ResponseUnion


class AuthMutation(graphene.Mutation):

    class Arguments(object):
        email = graphene.String()
        password = graphene.String()

    result = graphene.Field(AuthUnion)

    def mutate(self, info, **kwargs):
        user = User.objects(**kwargs).first()

        if user is not None:
            access_token = create_access_token(identity=kwargs["email"])
            refresh_token = create_refresh_token(identity=str(uuid4()))

            return AuthMutation(result=AuthField(access_token=access_token,
                                                 refresh_token=refresh_token,
                                                 message="Login Success"))
        else:
            return AuthMutation(result=AuthField(message="Login failed"))


class RefreshMutation(graphene.Mutation):

    class Arguments(object):
        refresh_token = graphene.String()

    result = graphene.Field(RefreshUnion)

    @classmethod
    @mutation_jwt_refresh_token_required
    def mutate(cls, _, **kwargs):
        return RefreshMutation(result=RefreshField(access_token=create_access_token(get_jwt_identity()),
                                                   message="Refresh success"))
