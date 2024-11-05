from django.urls import path, include

from rest_framework.routers import DefaultRouter

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LogoutView
from rest_framework_simplejwt.views import (
    TokenVerifyView
    , TokenRefreshView
    , TokenObtainPairView
)

from .views import UserProfileViewSet

router = DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='user-profile')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name="auth_obtain_rest"),
    path('token/refresh/', TokenRefreshView.as_view(), name="auth_refresh_rest"),
    path('token/verify/', TokenVerifyView.as_view(), name="auth_verify_rest"),
    path('register/', RegisterView.as_view(), name="auth_register_rest"),
    path('logout/', LogoutView.as_view(), name="auth_logout_rest"),

    path('', include(router.urls))
]