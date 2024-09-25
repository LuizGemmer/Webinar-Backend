from django.shortcuts import render

from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView
    , RetrieveUpdateDestroyAPIView
    , ListAPIView
)

from .models import Course, Function, Sector, Subsector
from .serializers_files.courses_serializers import AdminCourseSerializer
from .serializers_files.function_serializers import AdminFunctionSerializer
from .serializers_files.sector_serializers import AdminSectorSerializer
from .serializers_files.subsector_serializers import AdminSubsectorSerializer

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

#
# Sector views

class AdminSectorList(ListAPIView):
    queryset = Sector.objects.all()
    serializer_class = AdminSectorSerializer

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    

class AdminSectorDetails(RetrieveUpdateDestroyAPIView):
    queryset = Sector.objects.all()
    serializer_class = AdminSectorSerializer
    lookup_field = "id"

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class AdminSectorCreate(CreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = AdminSectorSerializer
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

#
# Subsector views

class AdminSubsectorList(ListAPIView):
    queryset = Subsector.objects.all()
    serializer_class = AdminSubsectorSerializer

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    

class AdminSubsectorDetails(RetrieveUpdateDestroyAPIView):
    queryset = Subsector.objects.all()
    serializer_class = AdminSubsectorSerializer
    lookup_field = "id"
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class AdminSubsectorCreate(CreateAPIView):
    queryset = Subsector.objects.all()
    serializer_class = AdminSubsectorSerializer
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

#
# Subsector views

class AdminFunctionList(ListAPIView):
    queryset = Function.objects.all()
    serializer_class = AdminFunctionSerializer

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    

class AdminFunctionDetails(RetrieveUpdateDestroyAPIView):
    queryset = Function.objects.all()
    serializer_class = AdminFunctionSerializer
    lookup_field = "id"
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class AdminFunctionCreate(CreateAPIView):
    queryset = Function.objects.all()
    serializer_class = AdminFunctionSerializer
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]