import graphene

from .idea import IdeasField


class ProfileField(graphene.ObjectType):
    img_path = graphene.String()
    email = graphene.String()
    username = graphene.String()
    rank = graphene.Int()
    point = graphene.Int()
    register_on = graphene.DateTime()
    my_ideas = graphene.List(IdeasField)
