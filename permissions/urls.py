from django.urls import path, include

from .view_files.fuctions_views import *
from .view_files.sector_views import *
from .view_files.subsector_views import *

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .view_files.sector_views import SectorViewSet, GetUserFunctionListView

sector_router = DefaultRouter()
sector_router.register(r'sector', SectorViewSet, basename="sector")

# Create your views here.
urlpatterns = [
    path('sector/get_logged_user_functions/', GetUserFunctionListView.as_view(), name="sector-get-logged-user-functions"),
    path('', include(sector_router.urls)),

    #TODO transform all into viewsets
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