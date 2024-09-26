import uuid

from django.db import models

class Sector(models.Model):
    '''
    Sector table model.
    Basic dimension table for segregating courses in the app.
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
        , unique = True
        , help_text = "Name of the sector. Must be unique."
    )

    description = models.TextField(
        help_text = "Specify what part of the organization this sector represents."
    )

    def __str__(self) -> str:
        return self.name