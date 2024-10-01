from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView
    , RetrieveUpdateDestroyAPIView
    , ListAPIView
)

from ..models import Course
from ..serializers_files.courses_serializers import UserCourseSerializer

from permissions.permission_service import PermissionService

class GetUserCourses(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = UserCourseSerializer

    permission_classes = []

    def get_queryset(self):
        user=self.request.user

        user_allowed_functions = PermissionService.get_user_functions(user)
        user_allowed_functions_ids = [instance.id for instance in user_allowed_functions]

        print(Course.objects.last().functions)

        return Course.objects.filter(coursefunction__id__in=user_allowed_functions_ids)

class GetCourseDetails():
    pass

