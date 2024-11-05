from rest_framework import serializers

from ..models import Sector

class AdminSectorSerializer(serializers.ModelSerializer):

    class Meta():
        model = Sector
        fields = [
            "id"
            , "name"
            , "description"
        ]
        read_only_fields = [
            "id"
        ]

class UserSectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ['name']