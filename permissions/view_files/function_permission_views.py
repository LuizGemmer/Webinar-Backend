
from rest_framework import viewsets, generics
from ..models import UserFunctionPermissions 

from ..serializers_files.function_permission_serializers import (
    FunctionPermissionViewSerializer,
    FunctionPermissionCreateSerializer
)

class FunctionPermissionsViewSet(viewsets.ModelViewSet):
    serializer_class = FunctionPermissionViewSerializer
    queryset = UserFunctionPermissions.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return self.serializer_class
        
        elif self.action in ['update', 'partial_update', 'create']:
            return FunctionPermissionCreateSerializer
        
        return super().get_serializer_class()

    def perform_update(self, serializer):
        # Update modified_by on update
        serializer.save(modified_by=self.request.user)

    def perform_create(self, serializer):
        # Set created_by and modified_by on creation
        serializer.save(created_by=self.request.user, modified_by=self.request.user)