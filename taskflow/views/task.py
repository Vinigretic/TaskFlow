from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from taskflow.models import Task, Project


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ('name', 'description', 'priority', 'deadline', 'status')
    template_name = 'taskflow/task_create.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def form_valid(self, form):
        project = Project.objects.get(id=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.get(id=self.kwargs['pk'])  # get project with help of id
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'taskflow/task_update.html'
    success_url = reverse_lazy('project_list_with_tasks')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'taskflow/task_delete.html'
    success_url = reverse_lazy('project_list_with_tasks')
