from rest_framework import serializers

from ..models import Subsector

from .function_serializers import EmbededFunctionSerializer

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

class SubsectorSerializer(serializers.ModelSerializer):
    functions = serializers.SerializerMethodField()

    class Meta:
        model = Subsector
        fields = ['id', 'name', 'functions']

    def get_functions(self, obj):
        user = self.context.get('user')
        functions = obj.functions.filter(user_functions__user=user)
        return EmbededFunctionSerializer(functions, many=True, context={'user': user}).data
