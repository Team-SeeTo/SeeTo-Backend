from app.models import Idea
from app.schema.fields import IdeasField, CommentField, ResponseMessageField

from flask_graphql_auth import query_jwt_required


@query_jwt_required
def resolve_ideas(root, info, **kwargs):

    search = kwargs.get('search_string', None)
    filter_by = kwargs.get('filter_by', None)
    view_id = kwargs.get('view', None)
    start_rank = kwargs.get('start_rank', 1) - 1

    if view_id is not None:
        idea = Idea.objects(id=view_id).first()

        if idea is None:
            return ResponseMessageField(is_success=False, message="Not found")

        return IdeasField(id=view_id,
                          author=idea.author.name,
                          title=idea.title,
                          body=idea.body,
                          created_at=idea.created_at,
                          upvoter=len([v.username for v in idea.upvoter]),
                          comments=[CommentField(author=c.author.username, body=c.body) for c in idea.comments],
                          category=idea.category)

    ideas = Idea.objects[start_rank: start_rank+30].order_by('point')

    if filter_by is not None:
        ideas = [idea for idea in ideas if idea.category == filter_by]

    if search is not None:
        ideas = [idea for idea in ideas if (search in idea.body) or (search in idea.title)]

    ideas = [IdeasField(id=str(idea.id),
                        author=idea.author.username,
                        title=idea.title,
                        body=idea.body,
                        created_at=idea.created_at,
                        upvoter=len([v.username for v in idea.upvoter]),
                        comments=[CommentField(author=c.author.username, body=c.body) for c in idea.comments],
                        category=idea.category) for idea in ideas]

    return ideas
