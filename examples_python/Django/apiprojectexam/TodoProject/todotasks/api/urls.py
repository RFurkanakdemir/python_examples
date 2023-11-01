
from django.urls import path , include
from todotasks.api import views as api_view

urlpatterns = [
    
    path('taskler/',api_view.TaskListCreateAPIView.as_view(),name='Task_listesi'),
    path('taskler/<int:pk>',api_view.TaskDetailAPIView.as_view(),name='Task_detay'),
]