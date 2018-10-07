import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity, AuthInfoField

from app.models import User, ToDo, Milestone, Type
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField

from app.schema.utils import todo_activity_logger


class CompleteToDoMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        id = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, id):
        todo = ToDo.objects(id=id).first()
        user = User.objects(email=get_jwt_identity(), todo=todo).first()

        if user is None:
            return CompleteToDoMutation(ResponseMessageField(is_success=False, message="Not Found"))

        try:
            todo.update(set__is_completed=True)
        except Exception as e:
            return CompleteToDoMutation(ResponseMessageField(is_success=False, message=str(e)))

        todo_activity_logger(user=user, type="todo")

        return CompleteToDoMutation(ResponseMessageField(is_success=True,
                                                         message="Todo complete success"))
