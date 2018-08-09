from app.schema.fields import TimeLimeField, ToDoReviewField, IdeasReviewField
from utils import constructor
from app.schema.utils import auth_required

from datetime import datetime


@auth_required
def resolve_timeline(root, info, date):
    return TimeLimeField(date=datetime.now(),
                         todo=ToDoReviewField(new_create=1,
                                              milestone_complete=1,
                                              todo_complete=1,
                                              total_point=10),
                         ideas=IdeasReviewField(new_vote=1,
                                                new_comment=1,
                                                new_create=1,
                                                total_point=10),
                         total_point=20)
