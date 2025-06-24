from django.db import models
from tasks import choices


class TaskList(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Task(models.Model):
    title = models.CharField(max_length=32)

    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    priority = models.CharField(choices=choices.TASKS_PRIORITIES, null=True, blank=True)

    repeat_after_seconds = models.IntegerField(null=True, blank=True)
    
    task_list = models.ForeignKey(TaskList, on_delete=models.PROTECT, related_name='tasks')
