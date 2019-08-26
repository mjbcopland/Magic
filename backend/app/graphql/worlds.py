from graphene_django.fields import DjangoListField

from app.models import World

from util.custom_types.graphene import Query

from .world import WorldObject


class WorldsQuery(Query):
    class Meta:
        output = DjangoListField(WorldObject, required=True).type

    def query(root, info, **kwargs):
        return World.objects.all()
