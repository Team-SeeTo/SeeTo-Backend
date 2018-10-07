import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User, Idea
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField

from app.schema.utils import idea_activity_logger


class VoteIdeaMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        id = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, id):
        user = User.objects(email=get_jwt_identity()).first()

        idea = Idea.objects(id=id).first()

        if idea is None:
            return VoteIdeaMutation(result=ResponseMessageField(is_success=False,
                                                                message="Not found"))

        if user not in idea.upvoter:
            try:
                idea.update(push__upvoter=user)
            except Exception as e:
                return VoteIdeaMutation(result=ResponseMessageField(is_success=False,
                                                                    message=str(e)))

            idea_activity_logger(user=user, type="vote")

            return VoteIdeaMutation(result=ResponseMessageField(is_success=True,
                                                                message="Vote success"))
        elif user in idea.upvoter:
            try:
                idea.update(pull__upvoter=user)
            except Exception as e:
                return VoteIdeaMutation(result=ResponseMessageField(is_success=False,
                                                                    message=str(e)))

            return VoteIdeaMutation(result=ResponseMessageField(is_success=True,
                                                                message="Vote cancel success"))

