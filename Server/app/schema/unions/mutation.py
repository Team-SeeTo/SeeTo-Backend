import graphene
from flask_graphql_auth import AuthInfoField

from app.schema.fields import ResponseMessageField, AuthField, RefreshField


class BaseUnion(graphene.Union):

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)


class ResponseUnion(BaseUnion):
    class Meta:
        types = (ResponseMessageField, AuthInfoField)


class AuthUnion(BaseUnion):
    class Meta:
        types = (AuthField, AuthInfoField)


class RefreshUnion(BaseUnion):
    class Meta:
        types = (RefreshField, AuthInfoField)
