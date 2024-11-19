from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .view_files.sector_views import SectorViewSet
from .view_files.subsector_views import SubsectorViewSet
from .view_files.fuctions_views import FunctionViewSet, GetUserFunctionListView


sector_router = DefaultRouter()
sector_router.register(r'sector', SectorViewSet, basename="sector")
sector_router.register(r'subsector', SubsectorViewSet, basename="subsector")
sector_router.register(r'function', FunctionViewSet, basename="function")

# Create your views here.
urlpatterns = [
    path('function/get_logged_user_functions/', GetUserFunctionListView.as_view(), name="sector-get-logged-user-functions"),
    path('', include(sector_router.urls)),
]