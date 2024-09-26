from django.db import models

from django.conf import settings

class UserPermissionTypes(models.Model):
    USER_PERMISSION_CHOICES = settings.USER_PERMISSION_CHOICES

    USER_PERMISSION_CONFIG = settings.USER_PERMISSION_CONFIG

    user_permission_type = models.CharField(
        choices=USER_PERMISSION_CHOICES
        , max_length=20
        , default=settings.VIEWER
    )