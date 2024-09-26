from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Function)
admin.site.register(Sector)
admin.site.register(Subsector)
admin.site.register(UserFunctionPermissions)
admin.site.register(UserSubsectorPermissions)
admin.site.register(UserSectorPermissions)

