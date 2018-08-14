from app.schema.fields import MirrorViewField, Growth
from app.schema.utils import auth_required
from utils import constructor


@auth_required
def resolve_mirror(root, info):
    growth = Growth(todo=1,
                    ideas=1,
                    total_point=2)

    return MirrorViewField(month=growth,
                           week=growth,
                           year=growth)