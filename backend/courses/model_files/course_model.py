import uuid

from django.db import models
from django.conf import settings


class Course(models.Model):
    '''
    Course table model
    Defines the table that holds the basic information of each course in the app.
    Each course will represent a skill desired of a worker, and inside of it there will be many classes
    designed to teach the specified skill
    '''

    id = models.UUIDField(
        primary_key=True
        , default=uuid.uuid4
        , editable=False
    )

    name = models.CharField(
        max_length=255
        , blank=False
        , null=False
        , help_text="Title/Name of the course"
    )

    description = models.TextField(
        help_text="A description of the course. use it to signal what it teaches, how the user should aprouch it and whatever else you like"
    )

    expiration_time_in_days = models.IntegerField(
        default=365
        , help_text='''
        How long it will take for the course certification to expire in days.
        If you want for it to not expire, set to a big number like: 99999
        '''
    )

    required_for_function = models.BooleanField(
        default = True
        , help_text = '''
        Defines if the course is needed for the function status to be set to "apt".
        If true, the user can only be "apt" if this course is completed.
        If false, this will be a complementary course, allowing the user to be "apt" even if not he has not compleated the course 
        '''
    )
    
    is_active = models.BooleanField(
        help_text="Soft delete boolean"
    ) 
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.CASCADE
        , related_name = 'created_courses'
    )

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.CASCADE
        , related_name = 'last_modified_courses'
    )