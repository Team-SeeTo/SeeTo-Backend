import graphene


class TypeEnum(graphene.Enum):
    INFINITY = 1
    STANDARD = 2
    HARD = 3


class Milestone(graphene.ObjectType):
    name = graphene.String()
    is_completed = graphene.Boolean()


class ToDoField(graphene.ObjectType):
    title = graphene.String()
    type = TypeEnum()
    created_at = graphene.DateTime()
    milestones = graphene.List(Milestone)
    expiration = graphene.DateTime()
    is_completed = graphene.Boolean()
