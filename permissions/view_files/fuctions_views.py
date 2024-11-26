
from rest_framework import permissions
from rest_framework import viewsets, generics
from rest_framework.response import Response

from ..models import Function, Sector

from ..serializers_files.function_serializers import AdminFunctionSerializer, FunctionSerializer
from ..serializers_files.sector_serializers import SectorSerializer

#
# funcion views
class FunctionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing function instances.
    """
    queryset = Function.objects.all()
    serializer_class = AdminFunctionSerializer

class GetUserFunctionListView(generics.ListAPIView):
    serializer_class = SectorSerializer
    
    def list(self, request, *args, **kwargs):
        sectors = Sector.objects.filter(
            subsectors__functions__user_functions__user=request.user
        ).prefetch_related(
            'subsectors__functions__user_functions'
        ).all().distinct()
        serializer = SectorSerializer(sectors, many=True, context={'user': request.user})
        return Response(serializer.data)
    
class GetFunctionByIdWithUserPercentComplete(generics.RetrieveAPIView):
    serializer_class = FunctionSerializer
    lookup_field = 'id'
    queryset = Function.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
    



    
    