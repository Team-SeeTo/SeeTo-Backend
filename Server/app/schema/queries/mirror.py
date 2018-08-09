from app.schema.fields import MirrorViewField, Growth
from app.schema.utils import auth_required
from utils import constructor


@auth_required
def resolve_mirror(root, info):
    growth = Growth(todo_growth_by_point=1,
                    ideas_growth_by_point=1,
                    total_point_growth_by_point=2)

    return MirrorViewField(month_growth=growth,
                           week_growth=growth,
                           year_growth=growth)