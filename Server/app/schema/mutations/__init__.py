import graphene
from app.schema.mutations.user.auth import AuthMutation, RefreshMutation
from app.schema.mutations.user.register import RegisterMutation


class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    register = RegisterMutation.Field()
