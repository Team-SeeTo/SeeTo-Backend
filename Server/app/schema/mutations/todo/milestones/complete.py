import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User, ToDo
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField

from app.schema.utils import todo_activity_logger


class CompleteMilestoneMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        todo_id = graphene.String()
        milestone_id = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, todo_id, milestone_id):
        todo = ToDo.objects(id=todo_id, milestones__id=milestone_id)
        user = User.objects(email=get_jwt_identity(), todo=todo.first()).first()

        if user is None:
            return CompleteMilestoneMutation(result=ResponseMessageField(is_success=False,
                                                                         message="Not found"))
        try:
            todo.update(set__milestones__S__is_completed=True)
        except Exception as e:
            return CompleteMilestoneMutation(result=ResponseMessageField(is_success=False,
                                                                         message=str(e)))

        todo_activity_logger(user=user, type="milestone")

        return CompleteMilestoneMutation(result=ResponseMessageField(is_success=True,
                                                                     message="Milestone complete success"))
