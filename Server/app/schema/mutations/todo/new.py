import graphene
from flask_graphql_auth import mutation_jwt_required, get_jwt_identity, AuthInfoField

from app.models import User, ToDo, Milestone, Type
from app.schema.unions import ResponseUnion
from app.schema.fields import ResponseMessageField

TypeEnum = graphene.Enum.from_enum(Type)


class NewToDoMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        title = graphene.String()
        type = TypeEnum()
        milestones = graphene.List(graphene.String)
        expiration = graphene.Date()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, title, milestones, type, expiration):
        user = User.objects(email=get_jwt_identity())

        type_enum = {1: "INFINITY", 2: "STANDARD", 3: "HARD"}
        type = type_enum.get(type, None)

        new_todo = ToDo(title=title,
                        type=str(type),
                        milestones=[Milestone(name=m) for m in milestones],
                        expiration=expiration)
        new_todo.save()

        user.update_one(inc__point=30)
        user.update_one(push__todo=new_todo)

        # User Log 남기는 기능은 함수로 따로 빼자

        return NewToDoMutation(ResponseMessageField(is_success=True,
                                                    message="Idea upload success"))
