import uuid

from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Quiz(models.Model):
    '''
    Quiz table model.
    Implements a basic quiz sistem, allowing the user to create quizes with multiple choice questions
    '''

    ## TODO: create a versioning system for the quiz, for better traceability of the results

    id = models.UUIDField(
        primary_key = True
        , default = uuid.uuid4
        , editable = False
    )

    name = models.CharField(
        max_length = 255
        , null = False
        , blank = False
        , help_text = "Name of the quiz (title)."
    )

    description = models.TextField(
        help_text = "Specify what the quiz is all about."
    )

    required_grade = models.IntegerField(
        null = False
        , blank = False
        , validators=[
            MaxValueValidator(100), MinValueValidator(0)
        ]
    )

    is_active = models.BooleanField(
        help_text="Soft delete boolean"
    ) 

    date_created = models.DateTimeField(auto_now_add=True)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.PROTECT
        , related_name = 'created_quizes'
    )

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.PROTECT
        , related_name = 'last_modified_quizes'
    )
    
    related_class = models.ForeignKey(
        settings.QUIZ_RELATED_CLASS_MODEL
        , on_delete = models.PROTECT
    )

    def delete(self, *args, **kwargs):
        # Soft delete - set is_active to False
        self.is_active = False
        self.save(update_fields=['is_active'])

    def __str__(self) -> str:
        return f'{self.related_class} - {self.name}'

    def question_count(self):
        return self.question_set.count()