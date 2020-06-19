from rest_framework.permissions import (
    BasePermission,

)

from users.models import UserRoles




class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and UserRoles.objects.filter(
                user=request.user, role__name="Admin"
            ).exists() )