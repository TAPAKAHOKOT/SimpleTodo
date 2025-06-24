from rest_framework import serializers
from tasks import choices, models

class TaskListSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=32)

    def create(self, validated_data):
        return models.TaskList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if not validated_data or 'name' not in validated_data:
            return instance
        
        instance.name = validated_data.get('name')
        instance.save()
        return instance

class TaskSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField(max_length=32)
    
    is_completed = serializers.BooleanField(required=False)
    completed_at = serializers.DateTimeField(required=False)

    priority = serializers.ChoiceField(choices.TASKS_PRIORITIES)

    repeat_after_minutes = serializers.IntegerField(required=False)
    task_list = serializers.PrimaryKeyRelatedField(queryset=models.TaskList.objects.all())

    def create(self, validated_data):
        return models.Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
            if hasattr(instance, field):
                setattr(instance, field, validated_data[field])
        
        instance.save()
        return instance
