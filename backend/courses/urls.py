from django.urls import path

from . import views


urlpatterns = [
    path("courses/", views.AdminCoursesList.as_view(), name="staff_course_list_rest"),
    path("courses/create/", views.AdminCoursesCreate.as_view(), name="staff_course_create_rest"),
    path("courses/<uuid:id>/", views.AdminCoursesDetails.as_view(), name="staff_course_details_rest"),
    path("courses/delete/<uuid:id>/", views.AdminCoursesDetails.as_view(), name="staff_course_delete_rest"),
    path("courses/update/<uuid:id>/", views.AdminCoursesDetails.as_view(), name="staff_course_update_rest"),

    path("sector/", views.AdminSectorList.as_view(), name="staff_sector_list_rest"),
    path("sector/create/", views.AdminSectorCreate.as_view(), name="staff_sector_create_rest"),
    path("sector/<uuid:id>/", views.AdminSectorDetails.as_view(), name="staff_sector_details_rest"),
    path("sector/delete/<uuid:id>/", views.AdminSectorDetails.as_view(), name="staff_sector_delete_rest"),
    path("sector/update/<uuid:id>/", views.AdminSectorDetails.as_view(), name="staff_sector_update_rest"),

    path("subsector/", views.AdminSubsectorList.as_view(), name="staff_subsector_list_rest"),
    path("subsector/create/", views.AdminSubsectorCreate.as_view(), name="staff_subsector_create_rest"),
    path("subsector/<uuid:id>/", views.AdminSubsectorDetails.as_view(), name="staff_subsector_details_rest"),
    path("subsector/delete/<uuid:id>/", views.AdminSubsectorDetails.as_view(), name="staff_subsector_delete_rest"),
    path("subsector/update/<uuid:id>/", views.AdminSubsectorDetails.as_view(), name="staff_subsector_update_rest"),

    path("function/", views.AdminFunctionList.as_view(), name="staff_function_list_rest"),
    path("function/create/", views.AdminFunctionCreate.as_view(), name="staff_function_create_rest"),
    path("function/<uuid:id>/", views.AdminFunctionDetails.as_view(), name="staff_function_details_rest"),
    path("function/delete/<uuid:id>/", views.AdminFunctionDetails.as_view(), name="staff_function_delete_rest"),
    path("function/update/<uuid:id>/", views.AdminFunctionDetails.as_view(), name="staff_function_update_rest"),
]