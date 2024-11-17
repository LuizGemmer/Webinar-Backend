import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone

from .course_model import Course

class UserCourseHistory(models.Model):
    '''
    Relates the user with the courses, providing a history of all times the user compleated it.
    Permissions to acces the courses are given by inserting the users to a function
    '''
    id = models.UUIDField(
        primary_key=True
        , default=uuid.uuid4
        , editable=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete=models.CASCADE
        , related_name='course_history'
    )

    course = models.ForeignKey(
        Course
        , on_delete=models.CASCADE
    )

    is_new_user = models.BooleanField(
        default=True
        , help_text="If true, it is the first time the user has done the course"
    )

    start_date = models.DateTimeField(
        null=True
        , help_text="Date of fisrt access of the user"
    )

    end_date = models.DateTimeField(
        null=True
        , help_text="Date the user finished the course"
    )

    is_submited = models.BooleanField(
        default=False
        , help_text="Signals if the user agreed to submit the course has finished"
    )

    date_submited = models.DateTimeField(
        null=True
        , help_text="Date the user submited the course"
    )

    expire_date = models.DateField(
        null=True
        , help_text="Date this couse expires, requiring the user to redo it"
    )

    def status(self):
        return self.is_submited and timezone.now() <= self.expire_date

    def is_current_valid_register(self):
        '''
        Defines if the history register is the current valid one.
        The user model will store always the next review and the previous reviews of the course
        So this method returns if it is the current one
        '''
        # TODO Implement
        return True

    