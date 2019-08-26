from graphene.types.mutation import Mutation, MutationOptions


class QueryOptions(MutationOptions):
    pass


class Query(Mutation):
    """
    Object Type Definition (query field)
    Query is a convenience type that helps us build a Field which takes Arguments and returns a
    query Output ObjectType.
    """

    @classmethod
    def mutate(cls, *args, **kwargs):
        query = getattr(cls, "query", None)
        assert query, "All queries must define a query method in it"
        return query(*args, **kwargs)
