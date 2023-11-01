from rest_framework import serializers
from todoapp.models import Task, Categorie
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


from datetime import datetime
from datetime import date
from django.utils.timesince import timesince

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model=Task
        exclude = ['owner']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['id',"username","is_staff","is_active"]


class CatSerializer(serializers.ModelSerializer):
    tasks= serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='task-detail',
    )

    class Meta:
        model = Categorie
        fields = '__all__'

