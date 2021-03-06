import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User, Idea
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class DeleteIdeaMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        id = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, id):
        user = User.objects(email=get_jwt_identity()).first()

        idea = Idea.objects(id=id, author=user).first()

        if idea is None:
            return DeleteIdeaMutation(result=ResponseMessageField(is_success=False,
                                                                  message="Not found"))

        try:
            idea.delete()
        except Exception as e:
            return DeleteIdeaMutation(result=ResponseMessageField(is_success=False,
                                                                  message=str(e)))

        # TODO: User Log 남기는 기능은 함수로 따로 빼자

        return DeleteIdeaMutation(result=ResponseMessageField(is_success=True,
                                                              message="Idea delete success"))
