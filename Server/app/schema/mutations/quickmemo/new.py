import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity, AuthInfoField

from app.models import User, QuickMemo
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class NewQuickMemoMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        title = graphene.String()
        body = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, title, body):
        user = User.objects(email=get_jwt_identity())

        new_memo = QuickMemo(title=title,
                             body=body)
        new_memo.save()

        user.update_one(push__quick_memo=new_memo)

        # TODO: User Log 남기는 기능은 함수로 따로 빼자

        return NewQuickMemoMutation(result=ResponseMessageField(is_success=True,
                                                                message="Quick memo upload success"))
