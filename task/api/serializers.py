from rest_framework import serializers
from . import models


class TaskManagementSerializer(serializers.ModelSerializer):

    assign_user_name = serializers.CharField(source='assign_user.username')
    create_user_name = serializers.CharField(source='created_by.username')

    class Meta:
        model = models.TaskManagement
        fields = ['task_no', 'task_description', 'start_time', 'end_time',
                  'assign_user', 'created_by', 'created_date', 'assign_user_name', 'create_user_name']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['user']
        task = models.TaskManagement(**validated_data)
        task.save()
        return task


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['username', 'last_name', 'id']

    def create(self, validated_data):
        user = models.TaskManagement(**validated_data)
        user.save()
        return user
