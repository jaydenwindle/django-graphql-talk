from rest_framework import viewsets

from todo.models import Todo
from todo.rest.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
