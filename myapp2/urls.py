from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.create_or_update_profile, name='profile'),

    path('task/list/', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'), 
    path('task/edit/<int:id>/', views.task_edit, name='task_edit'),
    path('task/delete/<int:id>/', views.task_delete, name='task_delete'),
 ]