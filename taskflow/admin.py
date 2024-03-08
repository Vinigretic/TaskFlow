from django.contrib import admin

from taskflow.models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'priority', 'status', 'created_at')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
