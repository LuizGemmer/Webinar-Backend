from rest_framework import viewsets, generics
from rest_framework.parsers import FormParser, MultiPartParser

from ..models import CourseClass
from ..serializers_files.class_course_serializers import UserClassSerializer

class UserClassViewSet(viewsets.ModelViewSet):
    '''
    View set to CRUD the items to the user
    '''
    queryset = CourseClass.objects.all()
    serializer_class = UserClassSerializer
    parser_classes = [FormParser, MultiPartParser]

    def perform_create(self, serializer):
        # Set created_by and modified_by on creation
        serializer.save(created_by=self.request.user, modified_by=self.request.user)

    def perform_update(self, serializer):
        # Update modified_by on update
        serializer.save(modified_by=self.request.user)

    def perform_destroy(self, instance):
        # Instead of deleting, set is_active to False (soft delete)
        instance.is_active = False
        instance.modified_by = self.request.user
        instance.save(update_fields=['is_active', 'modified_by'])

class GetClassesByCourse(generics.ListAPIView):
    '''
    Retrieve all classes of a course
    '''
    queryset = CourseClass.objects.all()
    serializer_class = UserClassSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('id')
        return CourseClass.objects.filter(course_id=course_id)