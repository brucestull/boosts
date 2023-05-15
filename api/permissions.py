from rest_framework.permissions import BasePermission

class IsRegistrationAccepted(BasePermission):
    def has_permission(self, request, view):
        return request.user.registration_accepted


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
