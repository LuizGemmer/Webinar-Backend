import uuid
from decimal import Decimal

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

    score = models.FloatField(
        null=True
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
        # Checks if the choice was already submited, if true, prevents the update
        if self.pk:
            # TODO check for a way to do this without this extra query to the database
            existing_instance = UserQuizScores.objects.filter(id=self.id)
            if len(existing_instance) != 0 and existing_instance[0].is_submited:
                raise ValidationError("Cannot update an already submited answer!")
            
        super().save(*args, **kwargs)

    # TODO set all models on the project to soft delete
    def delete(self, *args, **kwargs):
        # Soft delete - set is_active to False
        self.is_active = False
        self.save(update_fields=['is_active'])

    def __str__(self) -> str:
        return f'{self.user} - {self.quiz} - Submit: {self.date_submited}'

    def calculate_score(self):
        """
        Calculates the user score based on the number of correct questions
        score = questions in the quiz / correct answers * 100
        """
        question_count = self.quiz.question_count()

        if question_count == 0:
            raise ValidationError("cannot calculate the score of a quiz that has no questions!")

        user_correct_choices = self.userchoices_set.filter(is_correct=True).count()
        
        user_score = user_correct_choices / question_count * 100

        return round(user_score, 2)
        
    def quiz_score_above_required_score(self):
        """
        Checks if the score of the quiz atempt is greater or equal the quiz required grade
        """
        quiz_required_score = self.quiz.required_grade
        
        if self.score != None and quiz_required_score != None:
            return self.score >= quiz_required_score

        raise ValidationError("Either the quiz score or the required grade of the quiz is null!")