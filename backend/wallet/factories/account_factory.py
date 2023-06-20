import random
from datetime import datetime, timedelta

from django.utils import timezone
from factory import Faker
from factory.django import DjangoModelFactory

from wallet.enums import AccountType
from wallet.models import AccountModel, WalletModel


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = AccountModel

    name: str = Faker('name')
    type: str = None
    number: int = None
    open_date: datetime = None
    close_date: datetime = None

    @classmethod
    def create(cls, **kwargs):
        if not kwargs.get('number'):
            kwargs['number'] = cls.get_next_number()

        if not kwargs.get('open_date'):
            kwargs['open_date'] = datetime.now(tz=timezone.utc) - timedelta(days=random.choice(range(100, 10000)))

        if not kwargs.get('type'):
            kwargs['type'] = random.choice(AccountType.choices())[0]

        account = super().create(**kwargs)
        return account

    @classmethod
    def get_next_number(cls):
        last_number = AccountModel.objects.order_by('-number').first()

        return last_number.number + 1 if last_number else 1