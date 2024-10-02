
from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView
    , RetrieveUpdateDestroyAPIView
    , ListAPIView
)

from ..models import Function

from ..serializers_files.function_serializers import AdminFunctionSerializer

#
# funcion views

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