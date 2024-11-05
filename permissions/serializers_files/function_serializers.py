from rest_framework import serializers

from ..models import Function

from .subsector_serializers import UserSubsectorSerializer

class AdminFunctionSerializer(serializers.ModelSerializer):

    class Meta():
        model = Function
        fields = [
            "id"
            , "name"
            , "description"
            , "date_created"
            , "is_active"
        ]
        read_only_fields = [
            "id"
            , "date_created"
        ]

class UserFunctionSerializer(serializers.ModelSerializer):
    Subsector = UserSubsectorSerializer()

    class Meta:
        model = Function
        fields = ['name', 'Subsector', 'funtion_completion']

