import graphene


class TypeEnum(graphene.Enum):
    INFINITY = 1
    STANDARD = 2
    HARD = 3


class MilestoneField(graphene.ObjectType):
    name = graphene.String()
    is_completed = graphene.Boolean()


class ToDoField(graphene.ObjectType):
    title = graphene.String()
    type = graphene.String()
    created_at = graphene.DateTime()
    milestones = graphene.List(MilestoneField)
    expiration = graphene.DateTime()
    is_completed = graphene.Boolean()
