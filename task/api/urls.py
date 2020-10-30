from django.urls import path
from django.conf.urls import url
from .views import TaskManagement, TaskDetail, TaskUserList, UserList

urlpatterns = [
    path('task/', TaskManagement.as_view(), name='task-insert'),
    path('taskList/<int:pk>/', TaskDetail.as_view(), name='task-details'),
    path('taskUserList/<int:pk>/', TaskUserList.as_view(), name='task-details'),
    path('userlist/', UserList.as_view(), name='user-list'),

]
