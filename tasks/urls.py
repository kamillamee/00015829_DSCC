"""
URL configuration for tasks app.
"""
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/update/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('projects/<int:project_pk>/tasks/create/', views.task_create, name='task_create'),
    path('projects/<int:project_pk>/tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('projects/<int:project_pk>/tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
