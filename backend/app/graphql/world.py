from graphene_django.types import DjangoObjectType

import app.models.world


class WorldObject(DjangoObjectType):
    class Meta:
        model = app.models.world
