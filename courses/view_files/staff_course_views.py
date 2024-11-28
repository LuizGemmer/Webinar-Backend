from rest_framework import permissions
from rest_framework import viewsets

from ..models import Course
from ..serializers_files.courses_serializers import StaffCourseSerializer

class CoursesStaffViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing course instances with admin permissions.
    User will only be able to create courses for the sectors, subsectors and functions
    he is in. Except for staff and superusers. 
    """
    queryset = Course.objects.filter(is_active=True)
    serializer_class = StaffCourseSerializer

    def perform_create(self, serializer):
        # TODO evaluate user permissions
        serializer.save(created_by=self.request.user, modified_by=self.request.user)

    def perform_update(self, serializer):
        # TODO evaluate user permissions
        serializer.save(modified_by=self.request.user)

