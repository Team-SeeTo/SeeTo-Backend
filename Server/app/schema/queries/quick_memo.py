from app.schema.fields import QuickMemoField
from app.models import User

from flask_graphql_auth import get_jwt_identity, query_jwt_required


@query_jwt_required
def resolve_quick_memo(root, info):
    user = get_jwt_identity()
    memos = list(User.objects(email=user).first().quick_memo)

    memos.sort(key=lambda memo: memo.created_at)
    memos.reverse()

    return [QuickMemoField(title=m.title, body=m.body) for m in memos]
