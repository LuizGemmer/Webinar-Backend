from rest_framework import serializers

from django.db.models import Max

from ..models import Course, CourseFunction
from permissions.models import Function

class StaffCourseSerializer(serializers.ModelSerializer):
    function = serializers.CharField(write_only=True)

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
            , "function"
        ]
        read_only_fields = [
            "id"
            , "date_created"
            , "last_modified_date"
            , "created_by"
            , "modified_by"
        ]

    def create(self, validated_data):
        function = validated_data.pop('function', None)  # Pop the function argument if present

        instance = super().create(validated_data)

        if function:
            self.create_course_function_relation(function, instance)

        return instance

    def update(self, instance, validated_data):
        function = validated_data.pop('function', None)  # Pop the function argument if present

        # Perform your action with the function argument here
        # For example:
        if function:
            self.create_course_function_relation(function, instance)

        instance = super().update(instance, validated_data)
        return instance
    
    def create_course_function_relation(self, function, instance):
        has_function_relation = instance.course_functions.filter(
            course=self.instance, function=Function.objects.get(id=function)
        )

        if not has_function_relation:
            course_funtions = CourseFunction()
            course_funtions.course = instance
            course_funtions.function = Function.objects.get(id=function)

            course_funtions.save()


    def get_function(self, obj):
        return obj.courses_function.first().function.id

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
        read_only_fields = fields

class FunctionCoursesWithUserCompletePercentSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    expire_date = serializers.SerializerMethodField()
    class_file_type = serializers.SerializerMethodField()
    class_file = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'expire_date', 'status', 'class_file_type', 'class_file']

    def get_status(self, obj):
        user = self.context.get('user')
        history = [item for item in obj.user_history.filter(user=user)]
        if not len(history) == 0:
            current = [x for x in history if x.is_current_valid_register()]

            if not len(current) == 0:
                return current[0].status()
        
        return "pending"
        
    
    def get_expire_date(self, obj):
        user = self.context.get('user')

        max_expire_date = obj.user_history.filter(user=user).aggregate(
            max_date=Max('expire_date')
        )['max_date']
        
        return max_expire_date
    
    def get_class_file_type(self, obj):
        class_obj = obj.courseclass_set.first()
        class_file_type = class_obj.class_file_type if class_obj else ''
        return class_file_type if class_file_type else ''

    def get_class_file(self, obj):
        class_obj = obj.courseclass_set.first()
        class_file_type = class_obj.class_file.url if class_obj else ''
        return class_file_type if class_file_type else ''

