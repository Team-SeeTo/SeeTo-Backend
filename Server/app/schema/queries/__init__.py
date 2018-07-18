import graphene
from datetime import datetime
from app.schema.fields import *


class Query(graphene.ObjectType):
    profile = graphene.Field(type=ProfileField,
                             token=graphene.String())

    todo = graphene.List(of_type=ToDoField,
                         token=graphene.String(),
                         type=graphene.String(default_value=None),
                         order_by=graphene.String(default_value=None))

    ideas = graphene.List(of_type=IdeasField,
                          token=graphene.String(),
                          search_string=graphene.String(default_value=None),
                          order_by=graphene.String(default_value=None))

    quick_memo = graphene.List(of_type=QuickMemoField,
                               token=graphene.String())

    time_line = graphene.List(of_type=TimeLimeField,
                              token=graphene.String(),
                              date=graphene.DateTime(default_value=datetime.now()),
                              search_string=graphene.String(default_value=None),
                              order_by=graphene.String(default_value=None))

    mirror = graphene.List(of_type=MirrorViewField,
                           token=graphene.String(),
                           compare_range=graphene.Date())

    leaderboars = graphene.List(of_type=LeaderboardsField,
                                token=graphene.String())
