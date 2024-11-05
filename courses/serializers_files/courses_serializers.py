from rest_framework import serializers

from ..models import Course

class StaffCourseSerializer(serializers.ModelSerializer):

    class Meta():
        model = Course
        fields = [
            "id"
            , "name"
            , "description"
            , "expiration_time_in_days"
            , "required_for_function"
            , "is_active"
            , "date_created"
            , "last_modified_date"
            , "created_by"
            , "modified_by"
        ]
        read_only_fields = [
            "id"
            , "date_created"
            , "last_modified_date"
            , "created_by"
            , "modified_by"
        ]

class UserCourseSerializer(serializers.ModelSerializer):

    class Meta():
        model = Course
        fields = [
            "id"
            , "name"
            , "description"
            , "expiration_time_in_days"
            , "required_for_function"
            , "is_active"
            , "date_created"
            , "last_modified_date"
            , "created_by"
            , "modified_by"
        ]
        read_only_fields = [
            "id"
            , "date_created"
            , "last_modified_date"
            , "created_by"
            , "modified_by"
        ]