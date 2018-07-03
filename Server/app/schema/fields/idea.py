import graphene


class CommentField(graphene.ObjectType):
    author = graphene.String()
    body = graphene.String()


class IdeasField(graphene.ObjectType):
    author = graphene.String()
    title = graphene.String()
    body = graphene.String()
    created_at = graphene.DateTime()
    upvoter = graphene.List(graphene.String)
    comments = graphene.List(graphene.Field(CommentField))
