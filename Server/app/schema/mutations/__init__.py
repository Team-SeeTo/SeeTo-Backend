import graphene
from app.schema.mutations.user.auth import AuthMutation, RefreshMutation
from app.schema.mutations.user.register import RegisterMutation
from app.schema.mutations.todo import NewToDoMutation
from app.schema.mutations.quickmemo import NewQuickMemoMutation
from app.schema.mutations.idea import NewIdeaMutation
from app.schema.mutations.store import BuyItemMutation


class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    register = RegisterMutation.Field()

    new_todo = NewToDoMutation.Field()
    new_idea = NewIdeaMutation.Field()
    # new_comment = object
    new_quickmemo = NewQuickMemoMutation.Field()

    # edit_todo = object
    # edit_idea = object
    # edit_quickmemo = object

    # delete_todo = object
    # delete_idea = object
    # delete_comment = object
    # delete_quickmemo = object

    # check_milestone = object
    # delete_milestone = object

    buy_item = BuyItemMutation.Field()
    # spent_item = object




