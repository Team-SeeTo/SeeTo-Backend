import graphene


class QuickMemoField(graphene.ObjectType):
    title = graphene.String()
    body = graphene.String()
