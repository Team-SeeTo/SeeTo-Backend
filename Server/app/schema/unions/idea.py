import graphene
from app.schema.fields import *


class IdeasUnion(graphene.Union):
    class Meta:
        types = (ResponseMessageField, IdeasField)