from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos

# Create your views here.

def index (request):
    todo_list=Todos.objects.all()
    return render(request,"todoapp/index.html")

def about (request):
    return render(request,"templates/todoapp/about.html")