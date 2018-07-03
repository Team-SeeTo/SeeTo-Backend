import graphene


class StoreItemField(graphene.ObjectType):
    name = graphene.String()
    price = graphene.Int()
    effect = graphene.String()
