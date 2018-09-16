from app.schema.fields import ToDoField, TypeEnum, Milestone
from app.schema.utils import auth_required
from app.models import User

from flask_graphql_auth import get_jwt_identity


@auth_required
def resolve_todo(root, info, **kwargs):
    order = kwargs.get('order_by', None)
    search = kwargs.get('search_string', None)

    user = get_jwt_identity()
    todos = list(User.objects(email=user).first().todo)

    if order is not None:
        todos.sort(key=lambda todo: todo[order])

    if search is not None:
        todos = [t for t in todos if search in t.title]

    return [ToDoField(title=t.title,
                      type=t.type,
                      created_at=t.created_at,
                      milestones=[Milestone(name=m.name, is_completed=m.is_completed) for m in t.milestones],
                      expiration=t.expiration,
                      is_completed=t.is_completed) for t in todos]
