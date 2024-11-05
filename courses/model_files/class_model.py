import uuid

from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

from .course_model import Course


class CourseClass(models.Model):
    '''
    Course Class table model
    Defines the table that holds the basic information of each class in the app.
    Each class will represent a set of instructions 
    '''

    FILE_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('pdf', 'PDF'),
    ]

    id = models.UUIDField(
        primary_key=True
        , default=uuid.uuid4
        , editable=False
    )

    name = models.CharField(
        max_length=255
        , blank=False
        , null=False
        , help_text="Title/Name of the class"
    )

    description = models.TextField(
        help_text="A description of the class. use it to signal what it teaches, how the user should aprouch it and whatever else you like"
    )

    class_file = models.FileField(
        upload_to="courses/classes/"
        , help_text="The path to the file"
    )

    course = models.ForeignKey(
        Course
        , on_delete=models.PROTECT
    )

    sequence_in_course = models.IntegerField(
        validators=[MinValueValidator(1)]
        , help_text="Sets which sequence the classes in the course must be shown. Starts from 1"
    )

    class_file_type = models.CharField(
        max_length=5
        , choices=FILE_TYPES
        , help_text="Saves the type of file to be stored"
    )
    
    is_active = models.BooleanField(
        help_text="Soft delete boolean"
    ) 
    
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.CASCADE
        , related_name = 'created_classes'
    )

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.CASCADE
        , related_name = 'last_modified_classes'
    )

    def __str__(self) -> str:
        return self.name
    
    def delete(self, *args, **kwargs):
        # Soft delete - set is_active to False
        self.is_active = False
        self.save(update_fields=['is_active'])
