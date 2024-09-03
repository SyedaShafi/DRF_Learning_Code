from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        # print(request.user.is_authenticated)
        if request.user.is_authenticated:
            return True
        if request.method == 'GET':
            return True
        return False



