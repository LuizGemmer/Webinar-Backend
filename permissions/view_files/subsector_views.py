
from rest_framework import permissions
from rest_framework import viewsets

from ..models import Subsector

from ..serializers_files.subsector_serializers import AdminSubsectorSerializer

#
# Subsector views

class SubsectorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = Subsector.objects.all()
    serializer_class = AdminSubsectorSerializer