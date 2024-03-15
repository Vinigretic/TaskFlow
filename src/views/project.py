from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from src.forms import ProjectForm
from src.models import Project


class ProjectListView(ListView):
    """View displays a list of projects owned by the current user."""

    model = Project
    context_object_name = 'projects'
    template_name = 'src/project_list_with_tasks.html'

    def get_queryset(self):
        """Get the queryset of projects owned by the current user."""
        if self.request.user.is_authenticated:
            return Project.objects.filter(owner=self.request.user)
        else:
            return Project.objects.none()


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new project."""

    model = Project
    form_class = ProjectForm
    template_name = 'src/project_create.html'
    # deferred URL resolution
    success_url = reverse_lazy('project_list_with_tasks')

    def form_valid(self, form):
        """Add the current user as the owner of the new project."""
        # form.instance - model instance which is created through a form
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for updating an existing project."""

    model = Project
    form_class = ProjectForm
    template_name = 'src/project_update.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def test_func(self):
        """Check if the current user is the owner of the project."""
        return self.request.user == self.get_object().owner


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting an existing project."""

    model = Project
    template_name = 'src/project_delete.html'
    success_url = reverse_lazy('project_list_with_tasks')

    def test_func(self):
        """Check if the current user is the owner of the project."""
        return self.request.user == self.get_object().owner
