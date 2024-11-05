from rest_framework import serializers

from ..models import CourseClass

class UserClassSerializer(serializers.ModelSerializer):

    class Meta():
        model = CourseClass
        fields = [
            "id", "name", "course", "sequence_in_course", "class_file_type", "class_file"
        ]

