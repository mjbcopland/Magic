from graphene.types.mutation import Mutation, MutationOptions


class QueryOptions(MutationOptions):
    pass


class Query(Mutation):
    """
    Object Type Definition (query field)
    Query is a convenience type that helps us build a Field which takes Arguments and returns a
    query Output ObjectType.
    """

    @property
    def mutate(self):
        query = getattr(self, "query", None)
        assert query, "All queries must define a query method in it"
        return query
