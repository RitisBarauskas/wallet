import decimal
import random
from typing import List

from factory.django import DjangoModelFactory

from users.models import UserModel
from wallet.models import OperationModel, OperationTypeModel, TransactionModel, AccountModel
from wallet.factories import TransactionFactory


class OperationFactory(DjangoModelFactory):
    class Meta:
        model = OperationModel

    type: OperationTypeModel = None
    initiator: UserModel = None
    amount: decimal.Decimal = None
    transaction: TransactionModel = None

    @classmethod
    def create(cls, operation_types: List[OperationTypeModel], initiator: UserModel, account: AccountModel, **kwargs):

        if not operation_types:
            raise ValueError('Operation types is empty')

        kwargs['initiator'] = initiator
        kwargs['type'] = random.choice(operation_types)
        kwargs['amount'] = decimal.Decimal(random.randrange(100, 100000000)) / 100
        kwargs['transaction'] = TransactionFactory.create(
            amount=kwargs['amount'],
            account=account,
        )

        return super().create(**kwargs)

