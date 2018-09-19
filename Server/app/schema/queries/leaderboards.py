from app.schema.fields import LeaderboardsField
from app.schema.utils import auth_required
from app.models import User


@auth_required
def resolve_leaderboards(root, info):

    return [LeaderboardsField(rank=i+1, name=u.username, point=u.point) for i, u in enumerate(User.objects.order_by('-point'))]