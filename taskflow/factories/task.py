import datetime

import factory.fuzzy
from factory import SubFactory

from taskflow.factories.project import ProjectFactory
from taskflow.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    """Factory for generating instances of the Task model."""

    name = factory.Sequence(lambda x: f"Task_{x}")
    description = factory.fuzzy.FuzzyText()
    status = False
    project = SubFactory(ProjectFactory)  # ForeignKey
    priority = factory.fuzzy.FuzzyChoice(choices=["Low", "Medium", "High"])
    deadline = factory.fuzzy.FuzzyDate(datetime.date(2024, 1, 1))

    class Meta:
        model = Task
