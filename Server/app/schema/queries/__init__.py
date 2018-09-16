import graphene
from datetime import datetime

from app.schema.unions import IdeasUnion
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
                         order_by=graphene.String(),
                         search_string=graphene.String(),
                         resolver=resolve_todo
                         )

    ideas = graphene.List(of_type=IdeasUnion,
                          token=graphene.String(),
                          search_string=graphene.String(),
                          filter_by=graphene.String(),
                          start_rank=graphene.Int(),
                          resolver=resolve_ideas)

    quick_memo = graphene.List(of_type=QuickMemoField,
                               token=graphene.String(),
                               resolver=resolve_quick_memo)

    timeline = graphene.Field(type=TimeLimeField,
                              token=graphene.String(),
                              date=graphene.Date(default_value=datetime.now),
                              resolver=resolve_timeline)

    mirror = graphene.Field(type=MirrorViewField,
                            token=graphene.String(),
                            resolver=resolve_mirror)

    leaderboards = graphene.List(of_type=LeaderboardsField,
                                 token=graphene.String(),
                                 resolver=resolve_leaderboards)
