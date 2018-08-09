import graphene
from datetime import datetime
from app.schema.fields import *
from app.schema.queries.profile import resolve_profile
from app.schema.queries.ideas import resolve_ideas
from app.schema.queries.quick_memo import resolve_quick_memo
from app.schema.queries.todo import resolve_todo
from app.schema.queries.timeline import resolve_timeline
from app.schema.queries.mirror import resolve_mirror
from app.schema.queries.leaderboards import resolve_leaderboards


class Query(graphene.ObjectType):
    profile = graphene.Field(type=ProfileField,
                             token=graphene.String(),
                             resolver=resolve_profile)

    todo = graphene.List(of_type=ToDoField,
                         token=graphene.String(),
                         order_by=graphene.String(default_value=None),
                         xp_type=graphene.String(default_value=None),
                         search_string=graphene.String(default_value=None),
                         resolver=resolve_todo
                         )

    ideas = graphene.List(of_type=IdeasField,
                          token=graphene.String(),
                          search_string=graphene.String(),
                          order_by=graphene.String(),
                          resolver=resolve_ideas)

    quick_memo = graphene.List(of_type=QuickMemoField,
                               token=graphene.String(),
                               resolver=resolve_quick_memo)

    timeline = graphene.Field(type=TimeLimeField,
                              token=graphene.String(),
                              date=graphene.DateTime(default_value=datetime.now()),
                              resolver=resolve_timeline)

    mirror = graphene.Field(type=MirrorViewField,
                            token=graphene.String(),
                            resolver=resolve_mirror)

    leaderboards = graphene.List(of_type=LeaderboardsField,
                                 token=graphene.String(),
                                 resolver=resolve_leaderboards)
