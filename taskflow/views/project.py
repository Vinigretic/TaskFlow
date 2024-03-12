from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from taskflow.forms import ProjectForm
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
    form_class = ProjectForm
    template_name = 'taskflow/project_create.html'
    success_url = reverse_lazy('project_list_with_tasks')  # deferred URL resolution

    def form_valid(self, form):
        # add user
        form.instance.owner = self.request.user  # form.instance - model instance which is created through a form
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'taskflow/project_update.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def test_func(self):
        return self.request.user == self.get_object().owner  # if method return false method handle_no_permission make redirect

    def handle_no_permission(self):
        return redirect('project_list_with_tasks')  # belong to AccessMixin, but you can use it because UserPassesTestMixin


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'taskflow/project_delete.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def test_func(self):
        return self.request.user == self.get_object().owner

    def handle_no_permission(self):
        return redirect('project_list_with_tasks')
