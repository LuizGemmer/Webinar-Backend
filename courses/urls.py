from django.urls import path

from .view_files.admin_views import *
from .view_files.user_course_views import *

urlpatterns = [
    path("all/", AdminCoursesList.as_view(), name="staff_course_list_rest"),
    path("all/create/", AdminCoursesCreate.as_view(), name="staff_course_create_rest"),
    path("all/<uuid:id>/", AdminCoursesDetails.as_view(), name="staff_course_details_rest"),
    path("all/delete/<uuid:id>/", AdminCoursesDetails.as_view(), name="staff_course_delete_rest"),
    path("all/update/<uuid:id>/", AdminCoursesDetails.as_view(), name="staff_course_update_rest"),

    path("get_user_courses/", GetUserCourses.as_view(), name="get_user_courses")
]