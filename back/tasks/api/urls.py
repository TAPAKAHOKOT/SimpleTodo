from rest_framework import routers
from tasks.api import views

router = routers.SimpleRouter()
router.register('task-lists', views.TaskListViewSet)
router.register('tasks', views.TaskViewSet)

urlpatterns = router.urls
