from rest_framework import permissions


class UpdateUserProfilePermission(permissions.BasePermission):
    """ Allow users to update their own profiles """

    def has_object_permission(self, request, view, obj):
        """ Check if user is trying to update their own profile """

        return request.method in permissions.SAFE_METHODS or obj.id == request.user.id


class UpdateOwnStatusPermission(permissions.BasePermission):
    """ Allow users to update their status """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """ Check user is updating their own status """

        return request.method in permissions.SAFE_METHODS or obj.user_profile.id == request.user.id
