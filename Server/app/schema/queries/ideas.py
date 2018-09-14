from app.schema.fields import IdeasField, CommentField
from flask_graphql_auth import get_jwt_identity

from app.schema.utils import auth_required
from app.models import *
from app.schema.fields import *


@auth_required
def resolve_ideas(root, info, **kwargs):

    search = kwargs.get('search_string', None)
    filter_by = kwargs.get('filter_by', None)
    start_rank = kwargs.get('start_rank', None) - 1

    ideas = Idea.objects[start_rank: start_rank+30].order_by(Idea.point)

    if filter_by is not None:
        ideas = [idea for idea in ideas if idea.category == filter_by]

    if search is not None:
        ideas = [idea for idea in ideas if (search in idea.body) or (search in idea.title)]

    return ideas
