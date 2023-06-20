import factory

from users.models import AddressModel


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AddressModel

    street = factory.Faker("street_address")
    city = factory.Faker("city")
    country = factory.Faker("country")
    house = factory.Faker("building_number")
    flat = factory.Faker("building_number")
    is_primary = factory.Faker("boolean")