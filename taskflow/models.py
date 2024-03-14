from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    """Model representing a project."""

    name = models.CharField(
        max_length=250,
        verbose_name='Project name'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Project was created'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects'

    )

    def __str__(self):
        """Returns a string representation of the project."""
        return f'{self.name}'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_at']


class Task(models.Model):
    """Model representing a task."""

    class TaskStatusChoices(models.TextChoices):
        LOW = "L", "Low"
        MEDIUM = "M", "Medium"
        HIGH = "H", "High"

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    name = models.CharField(
        max_length=250,
        verbose_name='Task name'
    )
    description = models.TextField(
        verbose_name='Task description',
        null=True,
        blank=True,
    )
    priority = models.CharField(
        verbose_name='Task priority',
        max_length=1,
        choices=TaskStatusChoices.choices,
        default=TaskStatusChoices.LOW,
    )
    deadline = models.DateField(
        verbose_name='Task deadline',
        null=True,
        blank=True,
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Task status'
    )  # True - task is done, False - task is active

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Task was created'
    )

    def __str__(self):
        """Returns a string representation of the task."""
        return (f'Task - {self.name},'
                f'priority - {self.get_priority_display()},'
                f'execution status - {self.status}')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-created_at']
