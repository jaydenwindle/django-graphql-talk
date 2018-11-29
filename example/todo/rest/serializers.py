from rest_framework import serializers

from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'done', 'created_at', 'user')

class TodoWrappedSerializer(serializers.Serializer):
    text = serializers.CharField()
    model = TodoSerializer()

    def create(self, validated_data):
        return validated_data