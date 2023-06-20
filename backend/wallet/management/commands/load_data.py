from django.core.management.base import BaseCommand

from users.factories.user_factory import UserFactory
from wallet.factories import OperationFactory, WalletFactory
from wallet.constants import OPERATION_TYPES
from wallet.models import OperationTypeModel


class Command(BaseCommand):
    help = 'Load data from factories'

    def handle(self, *args, **kwargs):
        users = UserFactory.create_batch(10)

        current_operation_types = OperationTypeModel.objects.all()
        operation_types = [OperationTypeModel(name=ot[1]) for ot in OPERATION_TYPES]
        new_operation_types = [ot for ot in operation_types if ot.name not in [oot.name for oot in current_operation_types]]
        if new_operation_types:
            OperationTypeModel.objects.bulk_create(new_operation_types)
            current_operation_types = OperationTypeModel.objects.all()

        for user in users:
            wallet = WalletFactory.create(owner=user)
            self.stdout.write(self.style.SUCCESS('Create wallet for user %s' % user.email))

            for account in wallet.accounts.all():
                OperationFactory.create_batch(100, operation_types=current_operation_types, initiator=user, account=account)

        self.stdout.write(self.style.SUCCESS('Successfully load data'))
