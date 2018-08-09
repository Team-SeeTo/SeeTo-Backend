from app.schema.fields import IdeasField, CommentField
from utils import constructor
from app.schema.utils import auth_required


from datetime import datetime

@auth_required
def resolve_ideas(root, info, **kwargs):
    return [IdeasField(author="Lewis",
                       title="Title",
                       body="Body",
                       created_at=datetime.now(),
                       upvoter=["steve", 'david'],
                       comments=CommentField(author="steve",
                                             body="Great"))]
