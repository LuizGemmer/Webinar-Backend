from rest_framework import generics
from rest_framework.response import Response 

from ..models import UserCourseHistory, Course

from ..serializers_files.courses_serializers import FunctionCoursesWithUserCompletePercentSerializer

class GetUserCoursesByFunctionId(generics.ListAPIView):
    """
    A view to retrieve the courses of a given function and the progress of the user on them.
    """
    queryset = UserCourseHistory.objects.all()
    serializer_class = FunctionCoursesWithUserCompletePercentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FunctionCoursesWithUserCompletePercentSerializer(
            queryset, many=True, context={'user': request.user}
        )
        return Response(serializer.data)

    def get_queryset(self):
        function_id = self.kwargs.get('id')
        user = self.request.user

        courses = Course.objects.filter(
            course_functions__function_id = function_id,
            user_history__user = user
        ).prefetch_related(
            'user_history'
        )

        return courses