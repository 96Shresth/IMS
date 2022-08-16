from rest_framework import permissions
from .models import incident
from django.core.exceptions import PermissionDenied

class Owner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.reporter_name == request.user:
            return True

class PutClosed(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.incident_status == 'open' or obj.incident_status == 'in progress':
            return True

# class PerList(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_superuser:
            return True

# class IsPer(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request