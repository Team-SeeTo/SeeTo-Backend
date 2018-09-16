from app.schema.fields import LeaderboardsField
from app.schema.utils import auth_required


@auth_required
def resolve_leaderboards(root, info):
    return [LeaderboardsField(rank=1, name="user1", point=30),
            LeaderboardsField(rank=2, name="user2", point=20)]