import graphene

from graphene.types import Mutation
from graphene_django.types import DjangoObjectType

from app.models import World

from util.custom_types.graphene import Query
from util.custom_types.graphene_django import DjangoInputObjectType


class WorldObject(DjangoObjectType):
    class Meta:
        model = World


class WorldInputObject(DjangoInputObjectType):
    class Meta:
        model = World
        exclude = ("id",)


class WorldQuery(Query):
    class Meta:
        output = graphene.NonNull(WorldObject)

    class Arguments:
        id = graphene.ID(required=True)

    def query(root, info, **kwargs):
        pk = kwargs.get("id")
        return World.objects.get(pk=pk)


class CreateWorld(Mutation):
    class Meta:
        output = graphene.NonNull(WorldObject)

    class Arguments:
        world = graphene.Argument(WorldInputObject)

    def mutate(root, info, **kwargs):
        world = kwargs.get("world", {})
        return World.objects.create(**world)


class DeleteWorld(Mutation):
    class Meta:
        output = graphene.NonNull(WorldObject)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(root, info, **kwargs):
        pk = kwargs.get("id")

        world = World.objects.get(pk=pk)
        world.delete()

        return world


class UpdateWorld(Mutation):
    class Meta:
        output = graphene.NonNull(WorldObject)

    class Arguments:
        id = graphene.ID(required=True)
        world = graphene.Argument(WorldInputObject, required=True)

    def mutate(root, info, **kwargs):
        pk = kwargs.get("id")
        update = kwargs.get("world")

        world = World.objects.get(pk=pk)

        for key, value in update:
            setattr(world, key, value)

        world.save()
        world.refresh_from_db()

        return world
