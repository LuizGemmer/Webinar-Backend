from rest_framework import serializers

from ..models import Function, UserFunctionPermissions

class AdminFunctionSerializer(serializers.ModelSerializer):

    class Meta():
        model = Function
        fields = [
            "id"
            , "name"
            , "description"
            , "date_created"
            , "is_active"
        ]
        read_only_fields = [
            "id"
            , "date_created"
        ]


class FunctionSerializer(serializers.ModelSerializer):
    percent_completed = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Function
        fields = ['id', 'name', 'description', 'percent_completed', 'status']

    def get_percent_completed(self, obj):
        # Get the percent completed from the UserFunction model
        user = self.context.get('user')
        user_function = UserFunctionPermissions.objects.filter(user=user, function=obj).first()
        return user_function.percent_completed() if user_function else 0
    
    def get_status(self, obj):
        # Get the percent completed from the UserFunction model
        user = self.context.get('user')
        user_function = UserFunctionPermissions.objects.filter(user=user, function=obj).first()
        return user_function.status() if user_function else 0
