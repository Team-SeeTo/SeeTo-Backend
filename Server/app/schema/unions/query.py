import graphene
from app.schema.fields import *
from flask_graphql_auth import AuthInfoField


class IdeasUnion(graphene.Union):
    class Meta:
        types = (AuthInfoField, IdeasField)


class ProfileUnion(graphene.Union):
    class Meta:
        types = (AuthInfoField, ProfileField)


class ToDoUnion(graphene.Union):
    class Meta:
        types = (AuthInfoField, ToDoField)


class QuickMemoUnion(graphene.Union):
    class Meta:
        types = (AuthInfoField, QuickMemoField)


class TimeLineUnion(graphene.Union):
    class Meta:
        types = (AuthInfoField, TimeLineField)


class LeaderboardsUnion(graphene.Union):
    class Meta:
        types = (AuthInfoField, LeaderboardsField)