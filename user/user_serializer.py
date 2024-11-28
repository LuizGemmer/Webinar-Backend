from rest_framework import serializers

from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='profile.name')

    class Meta():
        model = User
        fields = [
            'id'
            , 'is_active'
            , 'is_staff'
            , 'is_superuser'
            , 'date_created'
            , 'last_login'
            , 'email'
            , 'name'
        ]    
        read_only_fields = ['is_active', 'is_staff', 'is_superuser', 'date_created', 'last_login', 'email']