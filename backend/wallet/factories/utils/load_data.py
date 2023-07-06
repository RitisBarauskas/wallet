from users.factories.user_factory import UserFactory
from wallet.constants import OPERATION_TYPES
from wallet.factories import WalletFactory, OperationFactory
from wallet.models import OperationTypeModel


def load_data(count_users=10, count_operations=100):

    users = UserFactory.create_batch(count_users)

    current_operation_types = OperationTypeModel.objects.all()
    operation_types = [OperationTypeModel(name=ot[1]) for ot in OPERATION_TYPES]
    new_operation_types = [ot for ot in operation_types if ot.name not in [oot.name for oot in current_operation_types]]
    if new_operation_types:
        OperationTypeModel.objects.bulk_create(new_operation_types)
        current_operation_types = OperationTypeModel.objects.all()

    for user in users:
        wallet = WalletFactory.create(owner=user)

        for account in wallet.accounts.all():
            OperationFactory.create_batch(count_operations, operation_types=current_operation_types, initiator=user, account=account)

    return True