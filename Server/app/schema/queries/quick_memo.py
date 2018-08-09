from app.schema.fields import QuickMemoField
from utils import constructor
from app.schema.utils import auth_required


@auth_required
def resolve_quick_memo(root, info):
    return [QuickMemoField(title="Title", body="Body")]*3
