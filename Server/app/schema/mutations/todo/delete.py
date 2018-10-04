import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User
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
        user = User.objects(email=get_jwt_identity()).first()

        todo = [todo for todo in user.todo if str(todo.id) == id]

        if todo == []:
            return DeleteToDoMutation(result=ResponseMessageField(is_success=False,
                                                                  message="Not found"))

        todo = todo[0]

        try:
            todo.delete()
        except Exception as e:
            return DeleteToDoMutation(result=ResponseMessageField(is_success=False,
                                                                  message=str(e)))

        # TODO: User Log 남기는 기능은 함수로 따로 빼자

        return DeleteToDoMutation(result=ResponseMessageField(is_success=True,
                                                              message="Todo delete success"))
