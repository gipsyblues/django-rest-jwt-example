from rest_framework import permissions


class IsOwnerOrReadyOnly(permissions.BasePermission):
    """
    Custom object-level permission to only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only to the owner of the object
        return obj.owner == request.user
