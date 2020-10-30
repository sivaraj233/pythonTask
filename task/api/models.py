from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)#auto_now_add is included-ANT-03July2018
    created_by = models.ForeignKey(User, related_name="created_by_%(app_label)s_%(class)s_related", on_delete= models.SET_NULL, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)#auto_now is included-ANT-03July2018
    modified_by = models.ForeignKey(User, related_name="modified_by_%(app_label)s_%(class)s_related", on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TaskManagement(BaseModel):
    objects = None
    task_no = models.IntegerField(null=True)
    task_description = models.TextField()
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    assign_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class TaskAssignUser(BaseModel):
    task_id = models.ForeignKey(TaskManagement, related_name='task_id', on_delete=models.SET_NULL, blank=True, null=True)
    assign_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assign_user', blank=True, null=True)