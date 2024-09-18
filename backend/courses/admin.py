from django.contrib import admin

from .models import (
    Course
    , Function
    , Sector
    , Subsector
)

# Register your models here.
admin.site.register(Course)
admin.site.register(Function)
admin.site.register(Sector)
admin.site.register(Subsector)
