from django.urls import path, include
from . import views

app_name='to_do_list'

urlpatterns = [
    path('',views.TaskListView.as_view(),name='all'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(),name='task_detail'),
    path('new/',views.CreateTaskView.as_view(),name='task_create'),
    path('task/<int:pk>/edit/', views.UpdateTaskView.as_view(),name='task_update'),
    path('task/<int:pk>/delete/', views.DeleteTaskView.as_view(),name='task_delete'),
]
