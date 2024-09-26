import uuid

from django.db import models
from django.conf import settings

from .user_permission_types_model import UserPermissionTypes
from ..models import Function

class UserFunctionPermissions(models.Model):
    '''
    Model resposible to dictate user object level permissions on the Funcion model
    '''

    id = models.UUIDField(
        default = uuid.uuid4
        , primary_key = True
        , editable=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete=models.CASCADE
    )

    function = models.ForeignKey(
        Function
        , on_delete=models.CASCADE
    )

    permission_type = models.CharField(
        max_length=20
        , choices=UserPermissionTypes.USER_PERMISSION_CHOICES
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete=models.CASCADE
        , related_name="function_permissions_set"
    )

    date_created = models.DateTimeField(
        auto_now_add=True
        , editable=False
    )

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete=models.CASCADE
        , related_name="function_permissions_modified"
    )

    last_modified_date = models.DateTimeField(
        auto_now=True
    )