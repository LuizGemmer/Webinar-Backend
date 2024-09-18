import uuid

from django.db import models

from .subsector_model import Subsector

class Function(models.Model):
    '''
    Function table model.
    Basic dimension table for designation the functions a worker can have in the subsector.
    A function is intended to group a set of skills expected of a worker in a subsector.
    Each of this skils will be represented by a course inside of the function.
    '''

    id = models.UUIDField(
        primary_key = True
        , default = uuid.uuid4
        , editable = False
    )

    name = models.CharField(
        max_length = 255
        , null = False
        , blank = False
        , help_text = "Name of the function."
    )

    description = models.TextField(
        help_text = "Specify what the function is all about."
    )

    is_active = models.BooleanField(
        help_text="Soft delete boolean"
    ) 
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    Subsector = models.ForeignKey(
        Subsector
        , on_delete = models.CASCADE
    )
