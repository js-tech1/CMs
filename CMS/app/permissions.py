from rest_framework import permissions

class PostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only authenticated users can create or update posts.
        if request.user.is_authenticated:
            return True
        else:
            return False
