import graphene

from todo.models import Todo
from todo.graphql.types import TodoType


class CreateTodoMutation(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        title = graphene.String()
        done = graphene.Boolean()
    
    @classmethod
    def mutate(cls, root, info, title, done, *args, **kwargs):
        user = info.context.user

        todo = Todo.objects.create(user=user, title=title, done=done)

        return CreateTodoMutation(todo=todo)