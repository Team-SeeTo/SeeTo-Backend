import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity, AuthInfoField

from app.models import User, StoreItem
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField


class BuyItemMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        item = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, name):
        user = User.objects(email=get_jwt_identity())
        item = StoreItem.objects(name=name).first()

        if (user.point - item.price) < 0:
            return BuyItemMutation(ResponseMessageField(is_success=False,
                                                        message="You don't have enough balance"))

        user.update_one(dec__point=item.price)
        user.update_one(push__my_items=item)

        # User Log 남기는 기능은 함수로 따로 빼자

        return ResponseMessageField(is_success=True,
                                    message="Payment success")
