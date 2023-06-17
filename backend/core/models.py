from django.db import models


class UUIDMixin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
    )

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

    class Meta:
        abstract = True
