from tasks.api import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import datetime

from tasks import models
from tasks.tasks import repeat_task


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = models.TaskList.objects.all()
    serializer_class = serializers.TaskListSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

    def mark_completion(self, is_completed: bool):
        task = self.get_object()

        task.is_completed = is_completed
        task.completed_at = datetime.datetime.now() if is_completed else None
        task.save()

        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def completed(self, request, pk=None):
        task = self.get_object()
        if task.repeat_after_minutes:
            repeat_task.apply_async(args=[{
                'title': task.title,
                'priority': task.priority,
                'repeat_after_minutes': task.repeat_after_minutes,
                'task_list_id': task.task_list.id,
            }], countdown=task.repeat_after_minutes)
        
        return self.mark_completion(True)

    @action(detail=True, methods=['post'])
    def uncompleted(self, request, pk=None):
        return self.mark_completion(False)
