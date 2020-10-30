from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import serializers, models
from rest_framework.response import Response

# Create your views here.


class TaskManagement(generics.ListCreateAPIView):
    serializer_class = serializers.TaskManagementSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        self.queryset = models.TaskManagement.objects.all()
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TaskDetail(APIView):
    serializer_class = serializers.TaskManagementSerializer
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        """
        Fetch corresponding task object
        :param pk: task id
        :return: task object
        """
        try:
            return models.TaskManagement.objects.get(id=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, **kwargs):
        """
        Fetch task score details
        :param request: NA
        :param kwargs: task id
        :return: task score details
        """
        pk = kwargs.get('pk')
        task = self.get_object(pk)
        serializer = self.serializer_class(task)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        """
        Updates Task details
        :param request: task details
        :param kwargs: task id
        :return: task details
        """
        pk = kwargs.get('pk')
        task = self.get_object(pk)
        serializer = self.serializer_class(instance=task, data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskUserList(generics.ListCreateAPIView):
    serializer_class = serializers.TaskManagementSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """list all Task list with custom pagination"""
        self.queryset = models.TaskManagement.objects.filter(assign_user=kwargs.get('pk'))
        return self.list(request, *args, **kwargs)


class UserList(generics.ListCreateAPIView):
    serializer_class = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = models.User.objects.all()
        return self.list(request, *args, **kwargs)
