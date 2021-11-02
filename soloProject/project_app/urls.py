from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('createtask', views.create),
    path('<int:task_id>/delete', views.delete_task),
    path('task/<int:task_id>', views.task),
]
