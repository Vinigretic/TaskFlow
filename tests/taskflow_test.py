from urllib.parse import urlparse

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from taskflow.models import Project, Task

User = get_user_model()


@pytest.mark.django_db
def test_create_project_successful(django_client, user):
    """Test case to verify successful creation of a project."""
    django_client.force_login(user)
    url = reverse("project_create")
    response = django_client.post(url, {'name': 'Test Project'})
    assert response.status_code == 302
    assert Project.objects.all().count() == 1


@pytest.mark.django_db
def test_create_project_failed(django_client):
    """
    Test create.

    Test to verify failed creation of a project if
    user is unauthenticated.
    """
    url = reverse("project_create")
    response = django_client.post(url)  # Отправка POST-запроса
    parsed_url = urlparse(response.url)
    path_without_params = parsed_url.path
    assert response.status_code == 302
    assert path_without_params == reverse('account_login')


@pytest.mark.django_db
def test_update_project_successful(django_client, user, project):
    """Test case to verify successful update of a project."""
    django_client.force_login(user)
    new_name = "New Project Name"
    url = reverse("project_update", kwargs={"pk": project.id})
    response = django_client.post(url, {'name': new_name})
    project.refresh_from_db()
    assert response.status_code == 302
    assert project.name == new_name
    assert Project.objects.all().count() == 1


@pytest.mark.django_db
def test_update_project_failed(django_client, project):
    """
    Test update project.

    Test to verify failed update of a project if
    user is unauthenticated or user is not the owner of the project.
    """
    url = reverse("project_update", kwargs={"pk": project.id})
    response = django_client.post(url)
    parsed_url = urlparse(response.url)
    path_without_params = parsed_url.path
    assert response.status_code == 302
    assert path_without_params == reverse('account_login')

    new_user = User.objects.create(
        username='testuser',
        password='testpassword'
    )
    django_client.force_login(new_user)
    response = django_client.post(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_project_successful(django_client, user, project):
    """Test case to verify successful deletion of a project."""
    django_client.force_login(user)
    url = reverse("project_delete", kwargs={"pk": project.id})
    response = django_client.post(url)
    assert response.status_code == 302
    assert Project.objects.all().count() == 0


@pytest.mark.django_db
def test_delete_project_failed(django_client, project):
    """
    Test delete project.

    Test to verify failed deletion of a project if
    user is unauthenticated or user is not the owner of the project.
    """
    url = reverse("project_delete", kwargs={"pk": project.id})
    response = django_client.post(url)
    parsed_url = urlparse(response.url)
    path_without_params = parsed_url.path
    assert response.status_code == 302
    assert path_without_params == reverse('account_login')
    assert Project.objects.all().count() == 1

    new_user = User.objects.create(
        username='testuser',
        password='testpassword'
    )
    django_client.force_login(new_user)
    response = django_client.post(url)
    assert response.status_code == 403
    assert Project.objects.all().count() == 1


@pytest.mark.django_db
def test_create_task_successful(django_client, user, project):
    """Test case to verify successful creation of a task."""
    django_client.force_login(user)
    url = reverse("task_create", kwargs={"pk": project.id})
    response = django_client.post(url, {'name': 'New Task',
                                        'description': 'New description',
                                        'status': False,
                                        'priority': 'M',
                                        'deadline': '2024-03-08'
                                        })
    assert response.status_code == 302
    assert Task.objects.all().count() == 1


@pytest.mark.django_db
def test_create_task_failed(django_client, project):
    """
    Test create task.

    Test to verify failed creation of a task if
    user is unauthenticated.
    """
    url = reverse("task_create", kwargs={"pk": project.id})
    response = django_client.post(url)
    parsed_url = urlparse(response.url)
    path_without_params = parsed_url.path
    assert response.status_code == 302
    assert path_without_params == reverse('account_login')


@pytest.mark.django_db
def test_update_task_successful(django_client, user, task):
    """Test case to verify successful update of a task."""
    django_client.force_login(user)
    new_task_name = 'New Task name'
    url = reverse("task_update", kwargs={"pk": task.id})
    response = django_client.post(url, {'name': new_task_name,
                                        'description': 'New description',
                                        'status': False,
                                        'priority': 'M',
                                        'deadline': '2024-03-08'
                                        })
    task.refresh_from_db()
    assert response.status_code == 302
    assert task.name == new_task_name
    assert Task.objects.all().count() == 1


@pytest.mark.django_db
def test_update_task_failed(django_client, task):
    """
    Test update task.

    Test to verify failed update of a task if
    user is unauthenticated or user is not the owner of the task.
    """
    url = reverse("task_update", kwargs={"pk": task.id})
    response = django_client.post(url)
    parsed_url = urlparse(response.url)
    path_without_params = parsed_url.path
    assert response.status_code == 302
    assert path_without_params == reverse('account_login')

    new_user = User.objects.create(
        username='testuser',
        password='testpassword'
    )
    django_client.force_login(new_user)
    response = django_client.post(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_task_successful(django_client, user, task):
    """Test case to verify successful deletion of a task."""
    django_client.force_login(user)
    url = reverse("task_delete", kwargs={"pk": task.id})
    response = django_client.post(url)
    assert response.status_code == 302
    assert Task.objects.all().count() == 0


@pytest.mark.django_db
def test_delete_task_failed(django_client, task):
    """
    Test delete task.

    Test case to verify failed delete of a task if
    user is unauthenticated or user is not the owner of the task.
    """
    url = reverse("task_delete", kwargs={"pk": task.id})
    response = django_client.post(url)
    parsed_url = urlparse(response.url)
    path_without_params = parsed_url.path
    assert response.status_code == 302
    assert path_without_params == reverse('account_login')
    assert Task.objects.all().count() == 1

    new_user = User.objects.create(
        username='testuser',
        password='testpassword'
    )
    django_client.force_login(new_user)
    response = django_client.post(url)
    assert response.status_code == 403
    assert Task.objects.all().count() == 1
