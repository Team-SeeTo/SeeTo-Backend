import graphene


class Growth(graphene.ObjectType):
    todo_growth_by_point = graphene.Int()
    ideas_growth_by_point = graphene.Int()
    total_point_growth_by_point = graphene.Int()


class MirrorViewField(graphene.ObjectType):
    month_growth = graphene.Field(Growth)
    week_growth = graphene.Field(Growth)
    year_growth = graphene.Field(Growth)
    # 상세 TimeLine 비교는 TimeLine 쿼리 사용
