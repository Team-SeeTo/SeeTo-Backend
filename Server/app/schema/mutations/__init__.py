import graphene
from app.schema.mutations.user.auth import AuthMutation, RefreshMutation
from app.schema.mutations.user.register import RegisterMutation
from app.schema.mutations.todo import NewToDoMutation
from app.schema.mutations.quickmemo import NewQuickMemoMutation, UpdateQuickMemoMutation, DeleteQuickMemoMutation
from app.schema.mutations.idea import NewIdeaMutation, NewCommentMutation, UpdateIdeaMutation, DeleteIdeaMutation, VoteIdeaMutation
from app.schema.mutations.store import BuyItemMutation


class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    register = RegisterMutation.Field()

    new_todo = NewToDoMutation.Field()
    new_idea = NewIdeaMutation.Field()
    new_comment = NewCommentMutation.Field()
    new_quickmemo = NewQuickMemoMutation.Field()

    # edit_todo = object
    edit_idea = UpdateIdeaMutation.Field()
    vote_idea = VoteIdeaMutation.Field()
    edit_quickmemo = UpdateQuickMemoMutation.Field()

    # vote_idea = object

    # delete_todo = object
    delete_idea = DeleteIdeaMutation.Field()
    delete_quickmemo = DeleteQuickMemoMutation.Field()

    # check_milestone = object
    # delete_milestone = object

    buy_item = BuyItemMutation.Field()
    # spent_item = object




