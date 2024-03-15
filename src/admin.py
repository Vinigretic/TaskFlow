from django.contrib import admin

from src.models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'priority', 'status', 'created_at')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
