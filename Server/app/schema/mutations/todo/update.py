import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity, AuthInfoField

from app.models import User, ToDo, Milestone, Type
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class UpdateToDoMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        id = graphene.String()
        new_title = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, id, new_title):
        todo = ToDo.objects(id=id).first()
        user = User.objects(email=get_jwt_identity(), todo=todo).first()

        if user is None:
            return UpdateToDoMutation(ResponseMessageField(is_success=False, message="Not Found"))

        try:
            todo.update(set__title=new_title)
        except Exception as e:
            return UpdateToDoMutation(ResponseMessageField(is_success=False, message=str(e)))

        # TODO: User Log 남기는 기능은 함수로 따로 빼자

        return UpdateToDoMutation(ResponseMessageField(is_success=True,
                                                       message="Todo update success"))
