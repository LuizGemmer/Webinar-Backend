
from django.contrib.auth import get_user_model

from rest_framework import serializers

from ..models import UserFunctionPermissions
from .function_serializers import EmbededFunctionSerializer

user = get_user_model()

class BasicUserSerializer(serializers.ModelSerializer):
    class Meta():
        model = user
        fields = ["id", "email"]
        read_only_fields=["email"]

class FunctionPermissionViewSerializer(serializers.ModelSerializer):
    function = EmbededFunctionSerializer()
    user = BasicUserSerializer()
    created_by = BasicUserSerializer()
    modified_by = BasicUserSerializer()

    class Meta():
        model = UserFunctionPermissions
        fields = [
            "id"
            , "user"
            , "function"
            , "permission_type"
            , "is_obsolete"
            , "created_by"
            , "date_created"
            , "modified_by"
            , "last_modified_date"
        ]
        read_only_fields = fields

class FunctionPermissionCreateSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserFunctionPermissions
        fields = [
            "id"
            , "user"
            , "function"
            , "permission_type"
            , "is_obsolete"
            , "created_by"
            , "date_created"
            , "modified_by"
            , "last_modified_date"
        ]
        read_only_fields = [
            "created_by"
            , "date_created"
            , "modified_by"
            , "last_modified_date"
        ]