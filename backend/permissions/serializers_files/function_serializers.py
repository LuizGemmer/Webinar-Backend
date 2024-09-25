from rest_framework import serializers

from ..models import Function

class AdminFunctionSerializer(serializers.ModelSerializer):

    class Meta():
        model = Function
        fields = [
            "id"
            , "name"
            , "description"
            , "subsector"
            , "date_created"
            , "is_active"
        ]
        read_only_fields = [
            "id"
            , "date_created"
        ]