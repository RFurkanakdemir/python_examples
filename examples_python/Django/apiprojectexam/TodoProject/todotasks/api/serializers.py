from rest_framework import serializers
from todotasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        # field= '__all__'
        fields = ['id', 'oncelik', 'icerik', 'bas_tarih','bit_tarih','is_active']


