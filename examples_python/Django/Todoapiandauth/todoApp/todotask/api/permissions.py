from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import serializers


class IsTaskUser(permissions.BasePermission):
    
    
    def has_object_permission(self, request, view, obj):
        
        return obj.owner==request.user


# class IsOwner(permissions.BasePermission):
#    def has_permission(self, request, view):
#         return request.user in  User.objects.ge
        

        