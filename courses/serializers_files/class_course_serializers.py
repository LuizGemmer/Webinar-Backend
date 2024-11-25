from rest_framework import serializers

from ..models import CourseClass

class UserClassSerializer(serializers.ModelSerializer):

    class Meta():
        model = CourseClass
        fields = '__all__'  # Include all fields or list specific fields
        read_only_fields = ('id', 'date_created', 'last_modified_date', 'created_by', 'modified_by')  # Read-only fields

