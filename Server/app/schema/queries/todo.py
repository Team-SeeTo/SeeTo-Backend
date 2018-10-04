from app.schema.fields import ToDoField, MilestoneField, ResponseMessageField
from app.models import User

from flask_graphql_auth import get_jwt_identity, query_jwt_required


@query_jwt_required
def resolve_todo(root, info, **kwargs):
    order = kwargs.get('order_by', None)
    search = kwargs.get('search_string', None)
    view_id = kwargs.get('view', None)

    user = get_jwt_identity()
    todos = list(User.objects(email=user).first().todo)

    if view_id is not None:
        todo = [todo for todo in todos if todo.id == view_id]

        if todo == []:
            return [ResponseMessageField(is_success=False, message="Not found")]

        todo = todo[0]

        return [ToDoField(id=str(todo.id),
                          title=todo.title,
                          type=todo.type,
                          created_at=todo.created_at,
                          milestones=[MilestoneField(id=m.id, name=m.name, is_completed=m.is_completed) for m in
                                      todo.milestones],
                          expiration=todo.expiration,
                          is_completed=todo.is_completed)]

    if order is not None:
        try:
            todos.sort(key=lambda todo: todo[order])
        except:
            return [ResponseMessageField(is_success=False, message="Invalid option")]

    if search is not None:
        todos = [t for t in todos if search in t.title]

    return [ToDoField(id=str(t.id),
                      title=t.title,
                      type=t.type,
                      created_at=t.created_at,
                      milestones=[MilestoneField(id=m.id, name=m.name, is_completed=m.is_completed) for m in t.milestones],
                      expiration=t.expiration,
                      is_completed=t.is_completed) for t in todos]
