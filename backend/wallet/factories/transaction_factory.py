import datetime
import decimal
import random

import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from wallet.models import TransactionModel, AccountModel


class TransactionFactory(DjangoModelFactory):
    class Meta:
        model = TransactionModel

    account: AccountModel = None
    amount_debit: decimal.Decimal = decimal.Decimal(0)
    amount_credit: decimal.Decimal = decimal.Decimal(0)
    date: datetime.datetime = None
    description: str = factory.Faker('text')

    @classmethod
    def create(cls, amount: decimal.Decimal, account: AccountModel, **kwargs):
        kwargs['account'] = account
        types = ['amount_debit', 'amount_credit']
        kwargs[random.choice(types)] = amount
        kwargs['date'] = cls.generate_date(account)

        return super().create(**kwargs)

    @classmethod
    def generate_date(cls, account: AccountModel):
        last_transaction = account.transactions.last()
        now = datetime.datetime.now(tz=timezone.utc)
        if last_transaction:
            new_date = last_transaction.date + datetime.timedelta(days=random.choice(range(1, 10)))
            if datetime.datetime.now(tz=timezone.utc) < new_date:
                new_date = now
        else:
            new_date = now

        return new_date
