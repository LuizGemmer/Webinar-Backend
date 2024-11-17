
from rest_framework import permissions, generics
from rest_framework import viewsets 
from rest_framework.response import Response

from ..models import Sector, UserFunctionPermissions

from ..serializers_files.sector_serializers import AdminSectorSerializer, SectorSerializer
#
# Sector views

class SectorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = Sector.objects.all()
    serializer_class = AdminSectorSerializer

class GetUserFunctionListView(generics.ListAPIView):
    serializer_class = SectorSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     # Fetch all functions related to the user via UserFunctionPermissions
    #     user_functions = UserFunctionPermissions.objects.filter(user=user).select_related("function__Subsector__sector")
        
    #     # Use a set to track sectors and subsectors
    #     sector_dict = {}

    #     for user_function in user_functions:
    #         function = user_function.function
    #         subsector = function.Subsector
    #         sector = subsector.sector

    #         if sector not in sector_dict:
    #             sector_dict[sector] = {
    #                 "id": sector.id,
    #                 "sector": sector,
    #                 "subsectors": {}
    #             }

    #         if subsector not in sector_dict[sector]["subsectors"]:
    #             sector_dict[sector]["subsectors"][subsector] = {
    #                 "id": subsector.id,
    #                 "subsector": subsector,
    #                 "functions": []
    #             }

    #         sector_dict[sector]["subsectors"][subsector]["functions"].append(function)

    #     # Format the queryset result
    #     queryset = []
    #     for sector_data in sector_dict.values():
    #         subsectors_list = []
    #         for subsector_data in sector_data["subsectors"].values():
    #             subsector_data["subsector"].functions = subsector_data["functions"]
    #             subsectors_list.append(subsector_data["subsector"])

    #         sector_data["sector"].subsectors_list = subsectors_list
    #         queryset.append(sector_data["sector"])

    #     return queryset

    def list(self, request, *args, **kwargs):
        sectors = Sector.objects.filter(
            subsectors__functions__user_functions__user=request.user
        ).prefetch_related(
            'subsectors__functions__user_functions'
        ).all().distinct()
        serializer = SectorSerializer(sectors, many=True, context={'user': request.user})
        return Response(serializer.data)
