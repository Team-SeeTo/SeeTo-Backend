import graphene


class LeaderboardsField(graphene.ObjectType):
    rank = graphene.Int()
    name = graphene.String()
    point = graphene.Int()
