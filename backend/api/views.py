from rest_framework import permissions, viewsets

from api.serializers import WalletSerializer, AccountSerializer, TransactionSerializer, OperationSerializer, AttachmentSerializer
from wallet.models import WalletModel, AccountModel, TransactionModel, OperationModel, AttachmentModel


class WalletViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wallets to be viewed or edited.
    """
    queryset = WalletModel.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = AccountModel.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transactions to be viewed or edited.
    """
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


class OperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows operations to be viewed or edited.
    """
    queryset = OperationModel.objects.all()
    serializer_class = OperationSerializer
    permission_classes = [permissions.IsAuthenticated]


class AttachmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows attachments to be viewed or edited.
    """
    queryset = AttachmentModel.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticated]
