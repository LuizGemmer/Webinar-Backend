from django.urls import path

from . import views


urlpatterns = [
    path("courses/", views.AdminCoursesList.as_view(), name="staff_course_list_rest"),
    path("courses/create/", views.AdminCoursesCreate.as_view(), name="staff_course_create_rest"),
    path("courses/<uuid:id>/", views.AdminCoursesDetails.as_view(), name="staff_course_details_rest"),
    path("courses/delete/<uuid:id>/", views.AdminCoursesDetails.as_view(), name="staff_course_delete_rest"),
    path("courses/update/<uuid:id>/", views.AdminCoursesDetails.as_view(), name="staff_course_update_rest"),
]