from app.schema.fields import QuickMemoField, ResponseMessageField
from app.models import User

from flask_graphql_auth import get_jwt_identity, query_jwt_required


@query_jwt_required
def resolve_quick_memo(root, info, **kwargs):
    view_id = kwargs.get('view', None)

    user = get_jwt_identity()
    memos = list(User.objects(email=user).first().quick_memo)

    memos.sort(key=lambda memo: memo.created_at)
    memos.reverse()

    if view_id is not None:
        memo = [memo for memo in memos if view_id == memo.id]

        if memo == []:
            return ResponseMessageField(is_success=False, message="Not found")

        memo = memo[0]
        return QuickMemoField(id=memo.id, title=memo.title, body=memo.body)

    return [QuickMemoField(id=m.id,title=m.title, body=m.body) for m in memos]
