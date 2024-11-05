from rest_framework import viewsets

from .models import User
from .user_serializer import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=user.id)