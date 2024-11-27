from rest_framework import serializers

from django.utils.timezone import now
from datetime import timedelta

from ..models import UserCourseHistory

class SubmitUserCourseHistorySerializer(serializers.ModelSerializer):
    
    class Meta():
        model = UserCourseHistory
        fields = ['id', 'user', 'course', 'is_submited', 'date_submited', 'expire_date']
        read_only_fields = ['id', 'user', 'is_submited', 'date_submited', 'expire_date']

    def create(self, validated_data):
        user = self.context.get('request').user
        course = validated_data['course']

        save_time = now()

        instance = UserCourseHistory()
        instance.user = user
        instance.course = course
        instance.start_date = save_time
        instance.is_new_user = True
        instance.is_submited = True
        instance.date_submited = save_time
        instance.end_date = save_time

        expire_date = save_time + timedelta(days=instance.course.expiration_time_in_days)
        instance.expire_date = expire_date.date()

        return instance