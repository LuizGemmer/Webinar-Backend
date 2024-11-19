from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .view_files.sector_views import SectorViewSet
from .view_files.subsector_views import SubsectorViewSet
from .view_files.fuctions_views import FunctionViewSet, GetUserFunctionListView
from .view_files.function_permission_views import FunctionPermissionsViewSet 

router = DefaultRouter()
router.register(r'sector', SectorViewSet, basename="sector")
router.register(r'subsector', SubsectorViewSet, basename="subsector")
router.register(r'function', FunctionViewSet, basename="function")
router.register(r'user_function', FunctionPermissionsViewSet, basename="user-function")

# Create your views here.
urlpatterns = [
    path('function/get_logged_user_functions/', GetUserFunctionListView.as_view(), name="sector-get-logged-user-functions"),
    path('', include(router.urls)),
]