from urllib import request
from rest_framework import permissions

class IsOwnerOrAsmin(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True
        if 'performer' in request.data:
            return request.data['performer'] == request.user.id
        return True


class StatusChangePerm(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if 'status' in request.data:

            if int(request.data['status']) - obj.status == 1:
                if obj.status < 4 and request.user == obj.performer:
                    return True
                if obj.status == 4 and request.user.is_superuser:
                    return True
            if  int(request.data['status']) - obj.status == -1:
                if obj.status <= 4 and request.user == obj.performer:
                    return True
                if obj.status > 3 and request.user.is_superuser:
                   return True
            return False
        return True


class TextChangePerm(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if 'text' in request.data:
            return obj.creator == request.user or request.user.is_superuser