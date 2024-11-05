
from rest_framework import permissions
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Sector, UserFunctionPermissions, Function

from ..serializers_files.sector_serializers import AdminSectorSerializer
#
# Sector views

class SectorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = Sector.objects.all()
    serializer_class = AdminSectorSerializer

    def perform_create(self, serializer):
        # Set created_by and modified_by on creation
        serializer.save(created_by=self.request.user, modified_by=self.request.user)

    def perform_update(self, serializer):
        # Update modified_by on update
        serializer.save(modified_by=self.request.user)

class GetUserFunctionListView(APIView):
    def get(self, request):
        # TODO find a way to make better code
        # Get the logged-in user
        user = request.user
        
        # Step 1: Get all functions related to the user via UserFunction table
        user_functions = UserFunctionPermissions.objects.filter(user=user).select_related("function__Subsector__sector")

        # Create a dictionary to hold sectors and their subsectors/functions
        sector_dict = {}

        for user_function in user_functions:
            function = user_function.function
            subsector = function.Subsector
            sector = subsector.sector

            if sector.name not in sector_dict:
                sector_dict[sector.name] = {
                    "name": sector.name,
                    "subsectors": {}
                }

            if subsector.name not in sector_dict[sector.name]["subsectors"]:
                sector_dict[sector.name]["subsectors"][subsector.name] = {
                    "name": subsector.name,
                    "functions": []
                }

            sector_dict[sector.name]["subsectors"][subsector.name]["functions"].append(function.name)

        # Convert the dictionary into a list of sectors
        sectors = []
        for sector_name, sector_data in sector_dict.items():
            subsectors_list = []
            for subsector_name, subsector_data in sector_data['subsectors'].items():
                subsectors_list.append({
                    "name": subsector_data['name'],
                    "functions": subsector_data['functions']
                })
            sectors.append({
                "name": sector_data['name'],
                "subsectors": subsectors_list
            })

        return Response(sectors)
