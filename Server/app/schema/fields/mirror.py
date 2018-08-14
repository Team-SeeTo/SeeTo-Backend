import graphene


class Growth(graphene.ObjectType):
    todo = graphene.Int()
    ideas = graphene.Int()
    total_point = graphene.Int()


class MirrorViewField(graphene.ObjectType):
    month = graphene.Field(Growth)
    week = graphene.Field(Growth)
    year = graphene.Field(Growth)
    # 상세 TimeLine 비교는 TimeLine 쿼리 사용
