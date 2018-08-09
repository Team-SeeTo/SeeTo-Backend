from app.schema.fields import ToDoField, TypeEnum, Milestone
from utils import constructor
from app.schema.utils import auth_required

from datetime import *


@auth_required
def resolve_todo(root, info, order_by, **kwargs):
    return [ToDoField(title="Title",
                      type=TypeEnum.STANDARD,
                      created_at=datetime.now(),
                      milestones=[
                                     Milestone(name="Milestone",
                                               is_completed=False)
                                 ] * 2,
                      expiration=datetime.now() + timedelta(days=10),
                      is_completed=False)] * 2
