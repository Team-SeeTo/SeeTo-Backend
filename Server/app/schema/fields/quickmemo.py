import graphene


class QuickMemoField(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    body = graphene.String()
