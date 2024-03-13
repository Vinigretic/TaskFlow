from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from taskflow.forms import TaskForm
from taskflow.models import Task, Project


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskflow/task_create.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def form_valid(self, form):
        project = Project.objects.get(id=self.kwargs['pk'])  # get project with help of id
        form.instance.project = project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.get(id=self.kwargs['pk'])  # add project to context
        return context


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskflow/task_update.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def test_func(self):
        return self.request.user == self.get_object().project.owner


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'taskflow/task_delete.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def test_func(self):
        return self.request.user == self.get_object().project.owner


class TaskUpdateCheckBoxView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('status',)
    success_url = reverse_lazy('project_list_with_tasks')
