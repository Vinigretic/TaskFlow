# Generated by Django 4.2 on 2024-03-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_alter_project_name_alter_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Project name'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Task name'),
        ),
    ]
