from rest_framework import generics

from ..models import UserFunctionPermissions
from ..serializers_files.reports_serializers import UserFunctionReviewsDoneOnYearSerializer

class UserFunctionReviewsDoneOnYear(generics.GenericAPIView):
    serializer_class = UserFunctionReviewsDoneOnYearSerializer
    
    def get_queryset(self):
        year = self.request.get('year')
        serializer = self.get_serializer()

        queryset = UserFunctionPermissions.objects.filter(expire_date__gte=year)

        filters = serializer.validated_data
        funtion_filtered = filters['function']
        subsector_filtered = filters['subsector']
        sector_filtered = filters['sector']

        if len(funtion_filtered):
            queryset = queryset.filter(function__in=funtion_filtered)
        if len(subsector_filtered):
            queryset = queryset.filter(function__subsector__in=subsector_filtered)
        if len(sector_filtered):
            queryset = queryset.filter(function__sector__in=sector_filtered)

        returnData = {}

        for userFunction in queryset:
            status = userFunction.status()
            returnData[status] += 1

        return returnData
