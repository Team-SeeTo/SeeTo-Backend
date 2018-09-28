import graphene


class CommentField(graphene.ObjectType):
    author = graphene.String()
    body = graphene.String()


class CommentResultField(graphene.ObjectType):
    comment_count = graphene.Int()
    comments = graphene.List(CommentField)


class IdeasField(graphene.ObjectType):
    id = graphene.String()
    author = graphene.String()
    title = graphene.String()
    body = graphene.String()
    created_at = graphene.DateTime()
    upvoter = graphene.Int()
    comments = graphene.Field(CommentResultField)
    category = graphene.String()
