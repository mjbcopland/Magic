import graphene


class Query(graphene.ObjectType):
    hello_world = graphene.NonNull(
        graphene.String, resolver=lambda root, info: "Hello, world!"
    )


schema = graphene.Schema(query=Query)
