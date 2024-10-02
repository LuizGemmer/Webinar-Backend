from django.urls import path

from .view_files.fuctions_views import *
from .view_files.sector_views import *
from .view_files.subsector_views import *

# Create your views here.
urlpatterns = [
    path("sector/", AdminSectorList.as_view(), name="staff_sector_list_rest"),
    path("sector/create/", AdminSectorCreate.as_view(), name="staff_sector_create_rest"),
    path("sector/<uuid:id>/", AdminSectorDetails.as_view(), name="staff_sector_details_rest"),
    path("sector/delete/<uuid:id>/", AdminSectorDetails.as_view(), name="staff_sector_delete_rest"),
    path("sector/update/<uuid:id>/", AdminSectorDetails.as_view(), name="staff_sector_update_rest"),

    path("subsector/", AdminSubsectorList.as_view(), name="staff_subsector_list_rest"),
    path("subsector/create/", AdminSubsectorCreate.as_view(), name="staff_subsector_create_rest"),
    path("subsector/<uuid:id>/", AdminSubsectorDetails.as_view(), name="staff_subsector_details_rest"),
    path("subsector/delete/<uuid:id>/", AdminSubsectorDetails.as_view(), name="staff_subsector_delete_rest"),
    path("subsector/update/<uuid:id>/", AdminSubsectorDetails.as_view(), name="staff_subsector_update_rest"),

    path("function/", AdminFunctionList.as_view(), name="staff_function_list_rest"),
    path("function/create/", AdminFunctionCreate.as_view(), name="staff_function_create_rest"),
    path("function/<uuid:id>/", AdminFunctionDetails.as_view(), name="staff_function_details_rest"),
    path("function/delete/<uuid:id>/", AdminFunctionDetails.as_view(), name="staff_function_delete_rest"),
    path("function/update/<uuid:id>/", AdminFunctionDetails.as_view(), name="staff_function_update_rest"),
]