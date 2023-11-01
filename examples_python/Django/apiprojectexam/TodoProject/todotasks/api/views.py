from todotasks.models import Task
from todotasks.api.serializers import TaskSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class TaskListCreateAPIView(APIView):
    def get(self,request):
        taskler=Task.objects.all()
        serializer=TaskSerializer(taskler,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class TaskDetailAPIView(APIView):
    def get_objects(self,pk):
        task_ins=get_object_or_404(Task,pk=pk)
        return task_ins

    def get(self,request,pk):
        task = self.get_objects(pk=pk)
        serializer=TaskSerializer(task)
        return Response(serializer.data)

    def put (self,request,pk):
        task = self.get_objects(pk=pk)
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializerstatus=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        task=self.get_objects(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        