from celery import shared_task
from tasks import models

@shared_task
def repeat_task(task_data):
    return models.Task.objects.create(**task_data)
