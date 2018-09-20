
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
            new_user = User(**kwargs)
            new_user.save()

        except Exception as e:
            print(str(e))
            return RegisterMutation(is_success=False, message="Registration Failure")

        return RegisterMutation(is_success=True, message="Successfully registered")