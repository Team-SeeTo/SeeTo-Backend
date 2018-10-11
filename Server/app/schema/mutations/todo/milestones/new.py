import graphene
from uuid import uuid4
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity, AuthInfoField

from app.models import User, ToDo, Milestone, Type
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class AppendMilestoneMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        id = graphene.String()
        new_milestone = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, id, new_milestone):
        todo = ToDo.objects(id=id)
        user = User.objects(email=get_jwt_identity(), todo=todo.first()).first()

        if user is None:
            return AppendMilestoneMutation(ResponseMessageField(is_success=False, message="Not Found"))

        try:
            todo.update(push__milestones=Milestone(id=uuid4().hex, name=new_milestone))
        except Exception as e:
            return AppendMilestoneMutation(ResponseMessageField(is_success=False, message=str(e)))

        # TODO: User Log 남기는 기능은 함수로 따로 빼자

        return AppendMilestoneMutation(ResponseMessageField(is_success=True,
                                                            message="Milestone append success"))
