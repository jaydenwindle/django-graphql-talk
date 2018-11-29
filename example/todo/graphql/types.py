from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from todo.models import Todo

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo

class UserType(DjangoObjectType):
    class Meta:
        model = User
        only_fields = ['id', 'first_name', 'lastname', 'username']