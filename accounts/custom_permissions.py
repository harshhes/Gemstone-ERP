from rest_framework.permissions import BasePermission
from .models import *

class IsDefaultRole(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == 'DE':
            return False
    def has_permission(self, request, view):
        return super().has_permission(request, view)

class IsBusinessOwner(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == 'BO':
            return True
        return False

class IsPurchaseManager(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == 'PM':
            return True
        return False


class IsAccountAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == 'AA': 
            if request.method == 'DELETE':
                return False
        return True


class IsSalesManager(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == 'SM': 
            return True
        
        return False