from app.schema.fields import ProfileField
from utils import constructor
from flask_graphql_auth import get_jwt_identity
from app.schema.utils import auth_required
from datetime import datetime
from app.models.user import User


@auth_required
def resolve_profile(root, info, **kwargs):
    user = get_jwt_identity()
    user = User.objects(email=user).first()

    return ProfileField(email=user.email,
                        username=user.username,
                        rank=user.rank,
                        point=user.point,
                        register_on=user.register_on)

