from django.db import models

from core.models import TimeStampMixin, SoftDeleteMixin, UUIDMixin
from users.models import UserModel
from wallet.enums import AccountType


class AccountModel(models.Model, TimeStampMixin, SoftDeleteMixin, UUIDMixin):
    name = models.CharField(max_length=100)
    type = models.CharField(choices=AccountType.choices(), max_length=20, blank=False, null=False)
    number = models.IntegerField()
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'
        ordering = ('open_date',)


class WalletModel(models.Model, TimeStampMixin, SoftDeleteMixin, UUIDMixin):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='wallets')
    accounts = models.ManyToManyField(AccountModel, through='AccountOfWalletModel')
    image = models.ImageField(upload_to='image_wallet', null=True)

    class Meta:
        verbose_name = 'Кошелёк'
        verbose_name_plural = 'Кошельки'
        ordering = ('created_at',)


class TransactionModel(models.Model, TimeStampMixin, SoftDeleteMixin, UUIDMixin):
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE, related_name='transactions')
    amount_debit = models.DecimalField(max_digits=10, decimal_places=2)
    amount_credit = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ('created_at',)


class AccountOfWalletModel(models.Model, TimeStampMixin, SoftDeleteMixin, UUIDMixin):
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE, related_name='wallets')
    wallet = models.ForeignKey(WalletModel, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        verbose_name = 'Счёт кошелька'
        verbose_name_plural = 'Счета кошельков'
        ordering = ('created_at',)


class OperationTypeModel(models.Model, TimeStampMixin, SoftDeleteMixin, UUIDMixin):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип операции'
        verbose_name_plural = 'Типы операций'
        ordering = ('name',)


class OperationModel(models.Model, TimeStampMixin, SoftDeleteMixin, UUIDMixin):
    transaction = models.ForeignKey(TransactionModel, on_delete=models.CASCADE, related_name='operations')
    type = models.ForeignKey(OperationTypeModel, on_delete=models.CASCADE, related_name='operations')
    initiator = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='operations', null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    attachments = models.ManyToManyField('AttachmentModel', through='AttachmentOfOperationModel')

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
        ordering = ('created_at',)


class AttachmentModel(models.Model, TimeStampMixin, SoftDeleteMixin, UUIDMixin):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='attachments')
    length = models.IntegerField()
    mime_type = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
        ordering = ('created_at',)


class AttachmentOfOperationModel(models.Model, TimeStampMixin, SoftDeleteMixin, UUIDMixin):
    attachment = models.ForeignKey(AttachmentModel, on_delete=models.CASCADE, related_name='operations')
    operation = models.ForeignKey(OperationModel, on_delete=models.CASCADE, related_name='attachments')

    class Meta:
        verbose_name = 'Вложение операции'
        verbose_name_plural = 'Вложения операций'
        ordering = ('created_at',)


class AggregateAmountOfAccountModel(models.Model, UUIDMixin):
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сумма агрегата'
        verbose_name_plural = 'Суммы агрегатов'
