from rest_framework import serializers

from ..models import Sector

from .subsector_serializers import SubsectorSerializer

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

class SectorSerializer(serializers.ModelSerializer):
    subsectors = serializers.SerializerMethodField()

    class Meta:
        model = Sector
        fields = ['id', 'name', 'subsectors']

    def get_subsectors(self, obj):
        user = self.context.get('user')
        subsectors = obj.subsectors.prefetch_related('functions__user_functions').all()
        return SubsectorSerializer(subsectors, many=True, context={'user': user}).data