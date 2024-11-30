from rest_framework import serializers

from django.db.models import Max

from ..models import Course, UserCourseHistory

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

