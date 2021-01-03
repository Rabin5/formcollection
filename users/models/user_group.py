from django.db import models

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class GlobalPermission(Permission):
    """A global permission, not attached to a model"""

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        ct, created = ContentType.objects.get_or_create(
            model=self._meta.verbose_name, app_label=self._meta.app_label,
        )
        self.content_type = ct
        super(GlobalPermission, self).save(*args)
