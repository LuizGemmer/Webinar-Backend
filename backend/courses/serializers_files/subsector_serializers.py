from rest_framework import serializers

from ..models import Subsector

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