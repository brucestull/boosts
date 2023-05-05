from rest_framework.permissions import BasePermission

class IsRegistrationAccepted(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.registration_accepted