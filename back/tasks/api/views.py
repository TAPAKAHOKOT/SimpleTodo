from tasks.api import serializers
from rest_framework import viewsets

from tasks import models

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = models.TaskList.objects.all()
    serializer_class = serializers.TaskListSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
