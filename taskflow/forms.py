from django import forms

from taskflow.models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name',)


class TaskForm(forms.ModelForm):
    # 2022-10-10 01:01:01
    class Meta:
        model = Task
        fields = ('name', 'description', 'priority', 'deadline', 'status')

