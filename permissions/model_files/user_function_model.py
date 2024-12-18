import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone

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
        ,related_name="user_functions"
    )

    permission_type = models.CharField(
        max_length=20
        , choices=UserPermissionTypes.USER_PERMISSION_CHOICES
    )

    is_obsolete = models.BooleanField(
        default=False
        , help_text="When true, mark that the user does not need to review this function courses anymore"
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete=models.CASCADE
        , related_name="function_permissions_set"
    )

    date_created = models.DateTimeField(
        auto_now_add=True
    )

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete=models.CASCADE
        , related_name="function_permissions_modified"
    )

    last_modified_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self) -> str:
        return f'{self.user} - {self.function} - {self.permission_type}'
    
    def percent_completed(self):
        courses_to_complete = self.function.function_courses.all().count()
        courses_completed = self.get_courses_completed().count()

        return courses_completed / courses_to_complete * 100
    
    def status(self):
        if self.is_obsolete:
            return "obsolete"
        
        if self.percent_completed() == 100:
            return "done"
        else:
            return "pending"
        
    def get_courses_completed(self):
        return self.user.course_history.filter(
            is_submited=True
            , expire_date__gte=timezone.now()
            , course__course_functions__function=self.function
        ).distinct('course_id')
    
    def save(self, *args, **kwargs):
        # Check if an instance with the same user and function already exists
        # Preventing duplicate permissions
        existing = UserFunctionPermissions.objects.filter(user=self.user, function=self.function).first()

        if existing and existing.id != self.id:
            # Update the existing record
            existing.permission_type = self.permission_type
            existing.is_obsolete = self.is_obsolete
            existing.modified_by = self.modified_by
            existing.save()
            return existing

        # If no record exists, proceed with normal save
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.user} & {self.function}'