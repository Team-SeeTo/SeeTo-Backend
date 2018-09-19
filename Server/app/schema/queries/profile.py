from app.schema.fields import ProfileField
from app.schema.utils import auth_required
from app.models.user import User

from flask_graphql_auth import get_jwt_identity


@auth_required
def resolve_profile(root, info):
    user = get_jwt_identity()
    user = User.objects(email=user).first()

    return ProfileField(email=user.email,
                        username=user.username,
                        rank=list(User.objects.order_by('-point')).index(user)+1,
                        point=user.point,
                        register_on=user.register_on)

