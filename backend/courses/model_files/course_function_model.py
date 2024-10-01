import uuid

from django.db import models

# FIXME: direct import from other app. Create a interface to make the hole app more portable.
from permissions.models import Function
from .course_model import Course

class CourseFunction(models.Model):
    '''
    Relates the courses to the functions where each course is needed
    '''
    id = models.UUIDField(
        primary_key=True
        , default=uuid.uuid4
        , editable=False
    )

    function = models.ForeignKey(
        Function
        , on_delete=models.CASCADE
        , related_name='functions'
    )

    course = models.ForeignKey(
        Course
        , on_delete=models.CASCADE
    )