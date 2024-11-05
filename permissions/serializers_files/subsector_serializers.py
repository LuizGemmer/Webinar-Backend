from rest_framework import serializers

from ..models import Subsector

from .sector_serializers import UserSectorSerializer

class AdminSubsectorSerializer(serializers.ModelSerializer):

    class Meta():
        model = Subsector
        fields = [
            "id"
            , "name"
            , "description"
            , "sector"
            , "date_created"
            , "is_active"
        ]
        read_only_fields = [
            "id"
            , "date_created"
        ]

class UserSubsectorSerializer(serializers.ModelSerializer):
    sector = UserSectorSerializer()

    class Meta:
        model = Subsector
        fields = ['name', 'sector']