from django.urls import path,include
from todotask.api import views as api_views



urlpatterns = [
    path('tasks/',api_views.TaskListCreateAPIView.as_view(), name='tasks'),
    path('tasks/<int:pk>', api_views.TaskDetailAPIView.as_view(), name= 'task-detail'),
    path('users/',api_views.UserListAPIVİEW.as_view(),name='users'),
    path('register/',api_views.UserRegisterAPIVİEW.as_view(),name='register'),
]