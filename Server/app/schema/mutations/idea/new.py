import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity, AuthInfoField

from app.models import User, Idea
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class NewIdeaMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        title = graphene.String()
        body = graphene.String()
        category = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, title, body, category):
        author = User.objects(email=get_jwt_identity())

        new_idea = Idea(author=author.first(),
                        title=title,
                        body=body,
                        category=category)
        new_idea.save()

        author.update_one(inc__point=50)
        author.update_one(push__ideas=new_idea)

        # TODO: User Log 남기는 기능은 함수로 따로 빼자

        return NewIdeaMutation(result=ResponseMessageField(is_success=True,
                                                           message="Idea upload success"))
