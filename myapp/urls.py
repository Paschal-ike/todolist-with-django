from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task_detail/<int:pk>/', views.task_details, name='task_details'),
    path('task_create/', views.task_create, name='task_create'),
    path('task_update/<int:pk>/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]

