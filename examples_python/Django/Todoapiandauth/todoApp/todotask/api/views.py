from todotask.models import Task
from todotask.api.serializers import TaskSerializer,UserSerializer, RegisterSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from django.contrib.auth.models import User
from requests import request
from todotask.api.permissions import IsTaskUser



class TaskListCreateAPIView(generics.ListCreateAPIView):
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(owner=user)

    # queryset=Task.objects.all().order_by('id')
    serializer_class=TaskSerializer
    #permissions
    permission_classes= [permissions.IsAuthenticated]
    #pagination
    # pagination_class=SmallPagination

    def perform_create(self, serializer):
        serializer.save( owner = self.request.user)

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(owner=user)
    serializer_class=TaskSerializer
    permission_classes=[IsTaskUser]


class UserListAPIVİEW(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAdminUser]


class UserRegisterAPIVİEW(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer