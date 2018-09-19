from app.schema.fields import TimeLineField, ToDoReviewField, IdeasReviewField
from app.models import User, UserLog

from flask_graphql_auth import get_jwt_identity, query_jwt_required


@query_jwt_required
def resolve_timeline(root, info, date):
    date = date().date()
    
    user = User.objects(email=get_jwt_identity()).first()
    timeline = [t for t in UserLog.objects(user=user) if t.date.date() == date][0]

    return TimeLineField(date=date,
                         todo=ToDoReviewField(**dict(timeline.ToDo.to_mongo())),
                         ideas=IdeasReviewField(**dict(timeline.Ideas.to_mongo())),
                         total_point=timeline.ToDo.total_point + timeline.Ideas.total_point)
