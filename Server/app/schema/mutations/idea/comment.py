import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User, Idea, Comment
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField

from app.schema.utils import idea_activity_logger


class NewCommentMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        id = graphene.String()
        comment = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, id, comment):
        user = User.objects(email=get_jwt_identity()).first()

        idea = Idea.objects(id=id).first()

        if idea is None:
            return NewCommentMutation(result=ResponseMessageField(is_success=False,
                                                                  message="Not found"))
        try:
            idea.update(push__comments=Comment(author=user, body=comment))
        except Exception as e:
            return NewCommentMutation(result=ResponseMessageField(is_success=False,
                                                                  message=str(e)))

        user.update(inc__point=10)

        idea_activity_logger(user=user, type="comment")

        return NewCommentMutation(ResponseMessageField(is_success=True,
                                                       message="Comment upload success"))
