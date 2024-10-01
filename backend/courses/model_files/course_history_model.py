import uuid

from django.db import models
from django.conf import settings

from .course_model import Course

class UserCourseHistory(models.Model):
    '''
    Relates the user with the courses, providing a history of all times the user compleated it.
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

    