from apps.user.models import User
from factory.django import DjangoModelFactory
from factory import Faker


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = Faker("email")
    password = Faker("password")

    @classmethod
    def create_staff_user(cls):
        return cls(is_active=True, is_staff=True)

    @classmethod
    def create_superuser(cls):
        return cls(is_active=True, is_staff=True, is_superuser=True)
