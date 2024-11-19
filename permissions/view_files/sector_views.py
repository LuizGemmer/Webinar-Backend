from rest_framework import viewsets 

from ..models import Sector

from ..serializers_files.sector_serializers import AdminSectorSerializer
#
# Sector views

class SectorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = Sector.objects.all()
    serializer_class = AdminSectorSerializer


