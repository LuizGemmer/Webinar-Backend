from .view_files.staff_course_views import *
from .view_files.user_course_views import *
from .view_files.class_course_views import *

from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses/admin', CoursesStaffViewSet, basename="courses-admin")
router.register(r'classes', UserClassViewSet, basename="class")

urlpatterns = [
    path('classes/get_classes_by_course_id/<uuid:id>', GetClassesByCourse.as_view(), name="class-by-course"),
    
    path('', include(router.urls)),

]

