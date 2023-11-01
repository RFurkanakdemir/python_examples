from django.urls import path,include
from todoapp.api import views as api_views



urlpatterns = [
    path('tasks/',api_views.TaskListCreateAPIView.as_view(), name='tasks'),
    path('tasks/<int:pk>', api_views.TaskDetailAPIView.as_view(), name= 'task-detail'),
    path('users/',api_views.UserListAPIVİEW.as_view(),name='users'),
   
    path('categories/',api_views.CategorieListCreateAPIView.as_view(),name='categories')
]