import uuid

from django.db import models
from django.conf import settings

from .question import Question

class Choices(models.Model):
    '''
    Choices table model.
    Choices for the questions.
    '''

    ## TODO: create a versioning system for the choices, for better traceability of the results

    id = models.UUIDField(
        primary_key = True
        , default = uuid.uuid4
        , editable = False
    )

    title = models.TextField(
        null = False
        , blank = False
        , help_text = "Title/text of the choice"
    )

    is_correct = models.BooleanField(
        help_text="Define if this is the correct answer to the question"
    )

    is_active = models.BooleanField(
        help_text="Soft delete boolean"
    ) 

    date_created = models.DateTimeField(auto_now_add=True)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.PROTECT
        , related_name = 'created_choices'
    )

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.PROTECT
        , related_name = 'last_modified_choices'
    )

    question = models.ForeignKey(
        Question 
        , on_delete=models.PROTECT
    )
    
    def delete(self, *args, **kwargs):
        # Soft delete - set is_active to False
        self.is_active = False
        self.save(update_fields=['is_active'])

    def __str__(self) -> str:
        return f'{self.title}'
