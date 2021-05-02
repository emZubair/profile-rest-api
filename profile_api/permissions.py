from rest_framework import permissions


class UpdateUserProfilePermission(permissions.BasePermission):
    """ Allow users to update their own profiles """

    def has_object_permission(self, request, view, obj):
        """ Check if user is trying to update their own profile """

        return request.method in permissions.SAFE_METHODS or obj.id == request.user.id
