from app.schema.fields import TimeLineField, ToDoReviewField, IdeasReviewField
from app.models import User, UserLog
from datetime import datetime

from flask_graphql_auth import get_jwt_identity, query_jwt_required


@query_jwt_required
def resolve_timeline(root, info, date):
    date = datetime.strptime(date, "%Y-%m-%d").date()

    user = User.objects(email=get_jwt_identity()).first()
    timeline = UserLog.objects(user=user, date=date).first()

    if timeline is None:
        return TimeLineField(date=date,
                             todo=ToDoReviewField(new_create=0,
                                                  todo_complete=0,
                                                  milestone_complete=0,
                                                  total_point=0),
                             ideas=IdeasReviewField(new_create=0,
                                                    new_vote=0,
                                                    new_comment=0,
                                                    total_point=0),
                             total_point=0)

    return TimeLineField(date=date,
                         todo=ToDoReviewField(new_create=timeline.todo.new_create,
                                              todo_complete=timeline.todo.todo_complete,
                                              milestone_complete=timeline.todo.milestone_complete,
                                              total_point=timeline.todo.total_point),
                         ideas=IdeasReviewField(new_create=timeline.idea.new_create,
                                                new_vote=timeline.idea.new_vote,
                                                new_comment=timeline.idea.new_comment,
                                                total_point=timeline.idea.total_point),
                         total_point=timeline.todo.total_point + timeline.idea.total_point)
