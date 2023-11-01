from rest_framework import generics
from todoapp.models import Task,Categorie
from todoapp.api.serializers import TaskSerializer,UserSerializer,CatSerializer
from rest_framework import permissions
from todoapp.api.permissions import IsTaskUser
from django.contrib.auth.models import User



class TaskListCreateAPIView(generics.ListCreateAPIView):
    
    def get_queryset(self):
    
        user = self.request.user
        return Task.objects.filter(owner=user)

    # queryset=Task.objects.all().order_by('id')
    serializer_class=TaskSerializer
    #permissions
    # permission_classes= [permissions.IsAuthenticated]
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
    # permission_classes=[IsTaskUser]


class UserListAPIVİEW(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAdminUser]




class CategorieListCreateAPIView (generics.ListCreateAPIView):
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Categorie.objects.filter(owner=user)
    serializer_class=CatSerializer
    # permission_classes=[IsTaskUser]