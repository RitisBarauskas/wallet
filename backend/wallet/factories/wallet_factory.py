from typing import List

from factory.django import DjangoModelFactory
from factory import Faker, SubFactory, post_generation

from users.models import UserModel
from wallet.models import WalletModel, AccountModel, TransactionModel, OperationModel, AttachmentModel
from wallet.factories import AccountFactory


class WalletFactory(DjangoModelFactory):
    class Meta:
        model = WalletModel

    name: str = Faker('name')
    owner: UserModel = None
    image: str = None

    @classmethod
    def create(cls, **kwargs):
        wallet = super().create(**kwargs)
        accounts = AccountFactory.create_batch(4)
        wallet.accounts.set(accounts)
        return wallet



