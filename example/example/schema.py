import graphene

from todo.graphql.queries import AllTodosQuery
from todo.graphql.mutations import CreateTodoMutation


class RootQuery(AllTodosQuery,
                graphene.ObjectType):
    pass


class RootMutation(graphene.ObjectType):
    create_todo = CreateTodoMutation.Field()
    pass

schema = graphene.Schema(query=RootQuery, mutation=RootMutation)