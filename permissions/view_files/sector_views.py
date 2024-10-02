
from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView
    , RetrieveUpdateDestroyAPIView
    , ListAPIView
)

from ..models import Sector 

from ..serializers_files.sector_serializers import AdminSectorSerializer

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