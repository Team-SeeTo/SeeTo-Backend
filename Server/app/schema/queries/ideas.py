from flask_graphql_auth import get_jwt_identity

from app.schema.utils import auth_required
from app.models import Idea
from app.schema.fields import IdeasField, CommentField


@auth_required
def resolve_ideas(root, info, **kwargs):

    search = kwargs.get('search_string', None)
    filter_by = kwargs.get('filter_by', None)
    start_rank = kwargs.get('start_rank', 1) - 1

    ideas = Idea.objects[start_rank: start_rank+30]\
        .order_by('point')
    print(dict(ideas[0].to_mongo()))

    if filter_by is not None:
        ideas = [idea for idea in ideas if idea.category == filter_by]

    if search is not None:
        ideas = [idea for idea in ideas if (search in idea.body) or (search in idea.title)]

    ideas = [IdeasField(author=idea.author.username,
                        title=idea.title,
                        body=idea.body,
                        created_at=idea.created_at,
                        upvoter=[v.username for v in idea.upvoter],
                        comments=[CommentField(author=c.author.username, body=c.body) for c in idea.comments],
                        category=idea.category) for idea in ideas]

    return ideas
