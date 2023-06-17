import uuid

from django.db import models
from django.utils import timezone


class UUIDMixin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4,
    )

    def save(self, *args, **kwargs):
        if self.__check_uuid():
            self.id = uuid.uuid4()
            super(UUIDMixin, self).save(*args, **kwargs)

        super(UUIDMixin, self).save(*args, **kwargs)

    def __check_uuid(self) -> bool:
        return self._meta.model.objects.filter(id=self.id).exists()

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    is_deleted = models.BooleanField(
        default=False,
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
