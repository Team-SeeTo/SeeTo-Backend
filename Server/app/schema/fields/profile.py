import graphene


class ProfileField(graphene.ObjectType):
    profilepic = graphene.String()
    email = graphene.String()
    username = graphene.String()
    rank = graphene.Int()
    point = graphene.Int()
    register_on = graphene.String()
