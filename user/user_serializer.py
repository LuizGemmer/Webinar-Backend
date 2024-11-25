from rest_framework.serializers import ModelSerializer

from .models import User

class UserProfileSerializer(ModelSerializer):
    class Meta():
        model = User
        fields = ['id', 'is_active', 'is_staff', 'is_superuser', 'date_created', 'last_login', 'email']
        read_only_fields = ['is_active', 'is_staff', 'is_superuser', 'date_created', 'last_login', 'email']