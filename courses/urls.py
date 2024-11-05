from django.urls import path

from .view_files.staff_course_views import *
from .view_files.user_course_views import *

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses/admin/', CoursesStaffViewSet, basename="courses-admin")

urlpatterns = [
    path('', include(router.urls)),

]