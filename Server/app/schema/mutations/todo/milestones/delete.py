import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User, ToDo
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class DeleteMilestoneMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        todo_id = graphene.String()
        milestone_id = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, todo_id, milestone_id):
        todo = ToDo.objects(id=todo_id, milestones__id=milestone_id).first()
        user = User.objects(email=get_jwt_identity(),
                            todo=todo).first()

        if user is None:
            return DeleteMilestoneMutation(result=ResponseMessageField(is_success=False,
                                                                       message="Not found"))

        try:
            todo.update(pull__milestones__id=milestone_id)

            return DeleteMilestoneMutation(result=ResponseMessageField(is_success=True,
                                                                       message="Milestone delete success"))
        except Exception as e:
            return DeleteMilestoneMutation(result=ResponseMessageField(is_success=False,
                                                                       message=str(e)))
