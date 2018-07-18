import graphene


class ToDoReviewField(graphene.ObjectType):
    new_create = graphene.Int()
    milestone_complete = graphene.Int()
    todo_complete = graphene.Int()
    total_point = graphene.Int()


class IdeasReviewField(graphene.ObjectType):
    new_vote = graphene.Int()
    new_comment = graphene.Int()
    new_create = graphene.Int()
    total_point = graphene.Int()


class TimeLimeField(graphene.ObjectType):
    date = graphene.DateTime()
    todo = graphene.Field(ToDoReviewField)
    ideas = graphene.Field(IdeasReviewField)
    total_point = graphene.Int()
