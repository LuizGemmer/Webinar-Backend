from rest_framework import serializers

from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='profile.name')
    about_me = serializers.CharField(source='profile.about_me')
    serial_number = serializers.CharField(source='profile.serial_number')

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
            , 'about_me'
            , 'serial_number'
        ]    
        read_only_fields = ['is_active', 'is_staff', 'is_superuser', 'date_created', 'last_login', 'email']

    def update(self, instance, validated_data):
        profile = instance.profile
        profile.name = validated_data['profile']['name']
        profile.about_me = validated_data['profile']['about_me']
        profile.serial_number = validated_data['profile']['serial_number']
        profile.save()

        return instance
