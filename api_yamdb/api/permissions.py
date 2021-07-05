from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    """
    Permission for admins.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser
        return False


class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Permission for safe methods and admins.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_superuser
        return False


class IsStaffOrOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or obj.author == request.user
