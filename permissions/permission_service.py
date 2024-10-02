from .models import *

from django.conf import settings

from .models import UserFunctionPermissions

class PermissionService():

    def get_user_functions(user):
        '''
        Get user function permissions.
        Returns a list of those function permissions
        '''
        return UserFunctionPermissions.objects.filter(user=user)
