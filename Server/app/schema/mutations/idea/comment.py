import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User, Idea, Comment
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class NewCommentMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        id = graphene.String()
        comment = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, id, comment):
        user = User.objects(email=get_jwt_identity())

        idea = Idea.objects(id=id).first()

        if idea is None:
            return NewCommentMutation(result=ResponseMessageField(is_success=False,
                                                                  message="Not found"))
        try:
            idea.update(push__comments=Comment(author=user, body=comment))
        except Exception as e:
            return NewCommentMutation(result=ResponseMessageField(is_success=False,
                                                                  message=str(e)))

        user.update_one(inc__point=10)

        # User Log 남기는 기능은 함수로 따로 빼자

        return NewCommentMutation(ResponseMessageField(is_success=True,
                                                       message="Comment upload success"))
