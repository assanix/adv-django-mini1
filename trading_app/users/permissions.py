from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """Access allowed only for users with the 'admin' role."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, "role", None) == "admin"

class IsTraderUser(BasePermission):
    """Access allowed only for users with the 'trader' role."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, "role", None) == "trader"

class IsSalesRepresentative(BasePermission):
    """Access allowed only for users with the 'sales_rep' role."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, "role", None) == "sales_rep"

class IsClient(BasePermission):
    """Access allowed only for users with the 'customer' role."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, "role", None) == "customer"
