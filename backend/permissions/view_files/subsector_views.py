
from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView
    , RetrieveUpdateDestroyAPIView
    , ListAPIView
)

from ..models import Subsector

from ..serializers_files.subsector_serializers import AdminSubsectorSerializer

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