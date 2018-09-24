from app.schema.fields import ProfileField, IdeasField, CommentField
from app.models.user import User

from flask_graphql_auth import get_jwt_identity, query_jwt_required


@query_jwt_required
def resolve_profile(root, info):
    user = get_jwt_identity()
    user = User.objects(email=user).first()

    my_ideas = [IdeasField(id=str(idea.id),
                           author=idea.author.username,
                           title=idea.title,
                           body=idea.body,
                           created_at=idea.created_at,
                           upvoter=len([v.username for v in idea.upvoter]),
                           comments=[CommentField(author=c.author.username, body=c.body) for c in idea.comments],
                           category=idea.category) for idea in user.ideas]

    return ProfileField(email=user.email,
                        username=user.username,
                        rank=list(User.objects.order_by('-point')).index(user) + 1,
                        point=user.point,
                        register_on=user.register_on,
                        my_ideas=my_ideas)
