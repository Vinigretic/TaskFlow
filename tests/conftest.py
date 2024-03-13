import pytest
from django.test import Client
from pytest_factoryboy import register

from taskflow.factories.project import ProjectFactory
from taskflow.factories.task import TaskFactory
from taskflow.factories.user import UserFactory

register(UserFactory)
register(ProjectFactory)
register(TaskFactory)


@pytest.fixture
def django_client():
    return Client()


@pytest.fixture
def user(db, user_factory):
    return user_factory.create()


@pytest.fixture
def project(db, user, project_factory):
    return project_factory.create(owner=user)


@pytest.fixture
def task(db, project, task_factory):
    return task_factory.create(project=project)
