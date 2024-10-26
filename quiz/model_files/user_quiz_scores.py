import uuid

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from .quiz import Quiz

class UserQuizScores(models.Model):
    '''
    UserQuizScores table model.
    Stores the results of the quizes of each user.
    '''

    id = models.UUIDField(
        primary_key = True
        , default = uuid.uuid4
        , editable = False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
        , on_delete=models.PROTECT
    )

    quiz = models.ForeignKey(
        Quiz 
        , on_delete=models.PROTECT
    )

    is_submited = models.BooleanField(
        default=False
        , help_text="Sets if the quiz was submited. When submited, only view operations are allowed on the object"
    )

    date_submited = models.DateTimeField(null=True)

    score = models.DecimalField(
        null=True
        , decimal_places=2
        , max_digits=3
        , help_text="The score of the user on the test, from 1 to 100."
    )

    is_aproved = models.BooleanField(
        default=False
        , help_text="Stores if the user has passed the test"
    )

    is_active = models.BooleanField(
        default=True
        , help_text="Stores if the user has passed the test"
    )

    def save(self, *args, **kwargs):
        if self.pk and self.is_submited:
            raise ValidationError("Cannot update an already submited answer!")
            
        super().save(*args, **kwargs)

    # TODO set all models on the project to soft delete
    def delete(self, *args, **kwargs):
        # Soft delete - set is_active to False
        self.is_active = False
        self.save(update_fields=['is_active'])

    def __str__(self) -> str:
        return f'{self.user} - {self.quiz} - Submit: {self.date_submited}'