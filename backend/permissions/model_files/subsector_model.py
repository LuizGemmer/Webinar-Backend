import uuid

from django.db import models

from .sector_model import Sector

class Subsector(models.Model):
    '''
    Subsector table model.
    Basic dimension table for segregating courses inside a sector in the app.
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
        , help_text = "Name of the subsector."
    )

    description = models.TextField(
        help_text = "Specify what part of the sector this subsector represents."
    )

    is_active = models.BooleanField(
        help_text="Soft delete boolean"
    ) 
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    sector = models.ForeignKey(
        Sector
        , on_delete = models.CASCADE
    )
