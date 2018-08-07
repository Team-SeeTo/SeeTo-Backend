
import graphene

from app.models import User


class RegisterMutation(graphene.Mutation):

    class Arguments(object):
        email = graphene.String()
        username = graphene.String()
        password = graphene.String()

    is_success = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, **kwargs):
        try:
            rank = User.objects.count() + 1
            kwargs.update({"rank": rank})

            new_user = User(**kwargs)
            new_user.save()

        except Exception as e:
            return RegisterMutation(is_success=False, message="Registration Failure")

        return RegisterMutation(is_success=True, message="Successfully registered")