from app.schema.fields import ProfileField
from utils import constructor
from app.schema.utils import auth_required
from datetime import datetime


@auth_required
def resolve_profile(root, info, **kwargs):
    return ProfileField(profilepic="<URL>",
                        email="test@seeto.services",
                        username="Lewis",
                        rank=1,
                        point=100,
                        register_on=datetime.now())

