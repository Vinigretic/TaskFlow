import factory.fuzzy
from factory import SubFactory

from src.factories.user import UserFactory
from src.models import Project


class ProjectFactory(factory.django.DjangoModelFactory):
    """Factory for generating instances of the Project model."""

    name = factory.Sequence(lambda x: f"Project_{x}")
    owner = SubFactory(UserFactory)  # ForeignKey

    class Meta:
        model = Project
