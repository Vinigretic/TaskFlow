from django import forms

from taskflow.models import Project, Task


class ProjectForm(forms.ModelForm):
    """Form for creating or updating a project."""

    class Meta:
        model = Project
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TaskForm(forms.ModelForm):
    """A form for creating or updating a task."""

    class Meta:
        model = Task
        fields = ('name', 'description', 'priority', 'deadline', 'status')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),
        }
