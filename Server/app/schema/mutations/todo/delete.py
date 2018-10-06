import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User, ToDo
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class DeleteToDoMutation(graphene.Mutation):
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
            return DeleteToDoMutation(result=ResponseMessageField(is_success=False,
                                                                  message="Not found"))
        try:
            user.update(pull__todo=todo)
            todo.delete()
        except Exception as e:
            return DeleteToDoMutation(result=ResponseMessageField(is_success=False,
                                                                  message=str(e)))

        # TODO: User Log 남기는 기능은 함수로 따로 빼자

        return DeleteToDoMutation(result=ResponseMessageField(is_success=True,
                                                              message="Todo delete success"))
