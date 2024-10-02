
from rest_framework.generics import (
    CreateAPIView
    , RetrieveUpdateDestroyAPIView
    , ListAPIView
)

from ..models import UserFunctionPermissions 

from ..serializers_files.sector_serializers import AdminSectorSerializer

#
# TODO: implement the views for permission setting
    