from rest_framework import serializers
from tasks import choices, models

class TaskListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)

    def create(self, validated_data):
        return models.TaskList.objects.create(**validated_data)

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    
    is_completed = serializers.BooleanField(required=False)
    completed_at = serializers.DateTimeField(required=False)

    priority = serializers.ChoiceField(choices.TASKS_PRIORITIES)

    repeat_after_minutes = serializers.IntegerField(required=False)
    task_list = serializers.PrimaryKeyRelatedField(queryset=models.TaskList.objects.all())

    def create(self, validated_data):
        return models.Task.objects.create(**validated_data)
