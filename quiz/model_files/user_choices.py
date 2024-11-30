import uuid

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from .user_quiz_scores import UserQuizScores
from .question import Question
from .choice import Choices

class UserChoices(models.Model):
    '''
    UserChoices table model.
    Stores the choices of the user in each question/quiz.
    '''

    id = models.UUIDField(
        primary_key = True
        , default = uuid.uuid4
        , editable = False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
        # TODO change all on_delete properties to models.PROTECT (on the whole project)
        , on_delete=models.PROTECT
    )

    ## Keeps a reference of the quiz ID in case the any foreing key relationship changes
    ## after the user submits the question.
    user_quiz = models.ForeignKey(
        UserQuizScores 
        , on_delete=models.PROTECT
    )

    ## Keeps a reference of the question ID in case the any foreing key relationship changes
    ## after the user submits the question.
    question = models.ForeignKey(
        Question 
        , on_delete=models.PROTECT
    )

    ## Keeps a reference of the choice ID in case the any foreing key relationship changes
    ## after the user submits the question.
    choice = models.ForeignKey(
        Choices 
        , on_delete=models.PROTECT
    )

    is_submited = models.BooleanField(
        default=False
        , help_text="Sets if the answer was submited. When submited, only view operations are allowed on the object"
    )

    is_correct = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
        , help_text="Soft delete boolean"
    )

    date_submited = models.DateTimeField(null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    
    last_modified_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Checks if the choice was already submited, if true, prevents the update
        if self.pk:
            # TODO check for a way to do this without this extra query to the database
            existing_instance = UserChoices.objects.filter(id=self.id)
            if len(existing_instance) != 0 and existing_instance[0].is_submited:
                raise ValidationError("Cannot update an already submited answer!")

        # TODO check if a choice already exists for the user and user_quiz_score

        # Sets the choice and question of the quiz
        self.question = self.choice.question

        # Checks if the selectec choise is marked as correct
        self.is_correct = self.choice.is_correct
            
        super().save(*args, **kwargs)

    # TODO set all models on the project to soft delete
    def delete(self, *args, **kwargs):
        # Soft delete - set is_active to False
        self.is_active = False
        self.save(update_fields=['is_active'])

    def __str__(self) -> str:
        return f'{self.user} - correct: {self.is_correct} - {self.choice}'