from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(UserCourseHistory)
admin.site.register(CourseFunction)
admin.site.register(CourseClass)


