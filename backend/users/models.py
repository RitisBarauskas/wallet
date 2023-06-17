from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import TimeStampMixin, UUIDMixin, SoftDeleteMixin


class UserModel(AbstractUser, TimeStampMixin, SoftDeleteMixin, UUIDMixin):
    roles = models.ManyToManyField('RoleModel', through='RoleOfUserModel')


class RoleModel(TimeStampMixin, SoftDeleteMixin, UUIDMixin, models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField('PermissionModel', through='PermissionOfRoleModel')

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        ordering = ('created_at',)


class RoleOfUserModel(TimeStampMixin, SoftDeleteMixin, UUIDMixin, models.Model):
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователей'
        ordering = ('created_at',)


class PermissionModel(TimeStampMixin, SoftDeleteMixin, UUIDMixin, models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Разрешение'
        verbose_name_plural = 'Разрешения'
        ordering = ('created_at',)


class PermissionOfRoleModel(TimeStampMixin, SoftDeleteMixin, UUIDMixin, models.Model):
    permission = models.ForeignKey(PermissionModel, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Разрешение роли'
        verbose_name_plural = 'Разрешения ролей'
        ordering = ('created_at',)


class ProfileModel(TimeStampMixin, SoftDeleteMixin, UUIDMixin, models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    avatars = models.ManyToManyField('AvatarModel', through='AvatarOfProfileModel')
    addresses = models.ManyToManyField('AddressModel', through='AddressOfProfileModel')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('created_at',)


class AvatarModel(TimeStampMixin, SoftDeleteMixin, UUIDMixin, models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars', null=True)
    length = models.IntegerField()
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Аватар'
        verbose_name_plural = 'Аватары'
        ordering = ('created_at',)


class AvatarOfProfileModel(TimeStampMixin, SoftDeleteMixin, UUIDMixin, models.Model):
    avatar = models.ForeignKey(AvatarModel, on_delete=models.CASCADE)
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Аватар профиля'


class AddressModel(TimeStampMixin, SoftDeleteMixin, UUIDMixin, models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    flat = models.CharField(max_length=100)
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ('created_at',)


class AddressOfProfileModel(TimeStampMixin, SoftDeleteMixin, UUIDMixin, models.Model):
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Адрес профиля'
        verbose_name_plural = 'Адреса профилей'
        ordering = ('created_at',)
