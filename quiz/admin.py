from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choices)
admin.site.register(UserChoises)
admin.site.register(UserQuizScores)
