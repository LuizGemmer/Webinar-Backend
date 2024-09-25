from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView
    , RetrieveUpdateDestroyAPIView
    , ListAPIView
)

from .models import Course
from .serializers_files.courses_serializers import AdminCourseSerializer

# Create your views here.
class AdminCoursesList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = AdminCourseSerializer

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    
class AdminCoursesDetails(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = AdminCourseSerializer
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class AdminCoursesCreate(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = AdminCourseSerializer
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

