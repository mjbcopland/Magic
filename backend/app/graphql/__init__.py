import graphene

from .world import WorldQuery, CreateWorld, DeleteWorld, UpdateWorld


class Query(graphene.ObjectType):
    hello_world = graphene.NonNull(graphene.String, resolver=lambda root, info: "Hello, world!")

    world = WorldQuery.Field()


class Mutation(graphene.ObjectType):
    create_world = CreateWorld.Field()
    delete_world = DeleteWorld.Field()
    update_world = UpdateWorld.Field()


# include any extra types which may not be introspected through root types
types = []


schema = graphene.Schema(query=Query, mutation=Mutation, types=types)
