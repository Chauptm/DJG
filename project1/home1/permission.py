from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

