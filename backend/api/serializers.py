from rest_framework import serializers

from wallet.models import AccountModel, WalletModel, TransactionModel, OperationModel, AttachmentModel


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletModel
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = '__all__'


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationModel
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachmentModel
        fields = '__all__'
