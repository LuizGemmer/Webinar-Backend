
from rest_framework import permissions
from rest_framework import viewsets

from ..models import Function

from ..serializers_files.function_serializers import AdminFunctionSerializer

#
# funcion views
class FunctionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = Function.objects.all()
    serializer_class = AdminFunctionSerializer