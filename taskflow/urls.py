from django.urls import path

from taskflow.views.project import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from taskflow.views.task import TaskCreateView, TaskUpdateView, TaskDeleteView, TaskUpdateCheckBoxView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list_with_tasks'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('task/<int:pk>/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/update/checkbox/', TaskUpdateCheckBoxView.as_view(), name='task_update_checkbox'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
]

