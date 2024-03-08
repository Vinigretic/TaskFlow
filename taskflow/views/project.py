from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from taskflow.models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'taskflow/project_list_with_tasks.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Project.objects.filter(owner=self.request.user)
        else:
            return Project.objects.none()


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ('name', )
    template_name = 'taskflow/project_create.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # form.instance - model instance which is created through a form
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ('name', )
    template_name = 'taskflow/project_update.html'
    success_url = reverse_lazy('project_list_with_tasks')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'taskflow/project_delete.html'
    success_url = reverse_lazy('project_list_with_tasks')
