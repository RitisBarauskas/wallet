import random
from typing import List

import factory

from users.factories.address_factory import AddressFactory
from users.models import ProfileModel, UserModel, AvatarModel, AddressModel


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProfileModel

    user: UserModel = None

    @classmethod
    def create(cls, **kwargs):
        profile = super().create(**kwargs)
        addresses = AddressFactory.create_batch(random.choice(range(1, 4)))
        profile.addresses.set(addresses)

        return profile


