from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from taskflow.forms import TaskForm
from taskflow.models import Task, Project


class TaskCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new task associated with a project."""

    model = Task
    form_class = TaskForm
    template_name = 'taskflow/task_create.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def form_valid(self, form):
        """Associate the task with the project specified in the URL."""
        # get project with help of id
        project = Project.objects.get(id=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Add the project to the context for template."""
        context = super().get_context_data(**kwargs)
        # add project to context
        context['project'] = Project.objects.get(id=self.kwargs['pk'])
        return context


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for updating an existing task."""

    model = Task
    form_class = TaskForm
    template_name = 'taskflow/task_update.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def test_func(self):
        """Check if the current user is the owner of the associated project."""
        return self.request.user == self.get_object().project.owner


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting an existing task."""

    model = Task
    template_name = 'taskflow/task_delete.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def test_func(self):
        """Check if the current user is the owner of the associated project."""
        return self.request.user == self.get_object().project.owner


class TaskUpdateCheckBoxView(LoginRequiredMixin, UpdateView):
    """View for updating the status checkbox of an existing task."""

    model = Task
    fields = ('status',)
    success_url = reverse_lazy('project_list_with_tasks')
