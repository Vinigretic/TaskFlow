import factory.fuzzy
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for generating instances of the User model."""

    username = factory.Sequence(lambda x: f"User_{x}")
    email = factory.LazyAttribute(
        lambda obj: f'{obj.username}@example.com')  # obj - factory object, user model instance

    class Meta:
        model = User
