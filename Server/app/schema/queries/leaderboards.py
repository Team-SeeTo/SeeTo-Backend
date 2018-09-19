from app.schema.fields import LeaderboardsField
from app.models import User

from flask_graphql_auth import query_jwt_required


@query_jwt_required
def resolve_leaderboards(root, info):

    return [LeaderboardsField(rank=i+1, name=u.username, point=u.point) for i, u in enumerate(User.objects.order_by('-point'))]