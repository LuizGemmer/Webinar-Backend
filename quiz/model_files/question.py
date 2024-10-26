import uuid

from django.db import models
from django.conf import settings

from .quiz import Quiz

class Question(models.Model):
    '''
    Question table model.
    Questions for the Quizes.
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
        , help_text = "title of the question."
    )

    quiz = models.ForeignKey(
        Quiz 
        , on_delete=models.PROTECT
    )

    is_active = models.BooleanField(
        help_text="Soft delete boolean"
    ) 

    date_created = models.DateTimeField(auto_now_add=True)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.PROTECT
        , related_name = 'created_questions'
    )

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete = models.PROTECT
        , related_name = 'last_modified_questions'
    )

    def delete(self, *args, **kwargs):
        # Soft delete - set is_active to False
        self.is_active = False
        self.save(update_fields=['is_active'])

    def __str__(self) -> str:
        return f'{self.title}'