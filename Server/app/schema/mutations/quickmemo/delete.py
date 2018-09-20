import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity

from app.models import User
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class DeleteQuickMemoMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        id = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, id):
        user = User.objects(email=get_jwt_identity()).first()

        memo = [memo for memo in user.quick_memo if memo.id == id]

        if memo == []:
            return DeleteQuickMemoMutation(result=ResponseMessageField(is_success=False,
                                                                       message="Not found"))

        memo = memo[0]

        try:
            memo.delete()
        except Exception as e:
            return DeleteQuickMemoMutation(result=ResponseMessageField(is_success=False,
                                                                       message=str(e)))

        # TODO: User Log 남기는 기능은 함수로 따로 빼자

        return DeleteQuickMemoMutation(result=ResponseMessageField(is_success=True,
                                                                   message="Memo delete success"))
