import factory

from users.factories.profile_factory import ProfileFactory
from users.models import UserModel


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    username: str = None
    email: str = factory.Faker('email')
    password: str = factory.Faker('password')
    first_name: str = factory.Faker('first_name')
    last_name: str = factory.Faker('last_name')
    is_active: bool = True
    is_staff: bool = False
    is_superuser: bool = False

    @classmethod
    def create(cls, **kwargs):
        if kwargs.get('username') is None:
            kwargs['username'] = cls.get_next_username()

        user = super().create(**kwargs)
        ProfileFactory.create(user=user)

        return user

    @classmethod
    def get_next_username(cls):
        return f'testuser_{cls._meta.model.objects.count() + 1}'




