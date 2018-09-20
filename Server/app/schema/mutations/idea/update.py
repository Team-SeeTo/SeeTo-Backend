import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User, Idea
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class UpdateIdeaMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        id = graphene.String()
        update = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, id, update):
        user = User.objects(email=get_jwt_identity()).first()

        idea = Idea.objects(id=id, author=user).first()

        if idea is None:
            return UpdateIdeaMutation(result=ResponseMessageField(is_success=False,
                                                                  message="Not found"))

        try:
            idea.update(set__body=update)
        except Exception as e:
            return UpdateIdeaMutation(result=ResponseMessageField(is_success=False,
                                                                  message=str(e)))

        # TODO: User Log 남기는 기능은 함수로 따로 빼자

        return UpdateIdeaMutation(result=ResponseMessageField(is_success=True,
                                                              message="Idea update success"))
