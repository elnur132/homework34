from django.urls import path
from . import views

urlpatterns = [
    path('', views.HabitListView.as_view(), name='habit-list'),
    path('habits/create/', views.HabitCreateView.as_view(), name='habit-create'),
    path('habits/<int:habit_id>/', views.HabitUpdateView.as_view(), name='habit-update'),
    path('habits/<int:habit_id>/delete/', views.HabitDeleteView.as_view(), name='habit-delete'),
    path('habits/<int:habit_id>/tasks/', views.TaskListView.as_view(), name='task-list'),
    path('habits/<int:habit_id>/tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('habits/<int:habit_id>/tasks/<int:task_id>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('habits/<int:habit_id>/tasks/<int:task_id>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

]
