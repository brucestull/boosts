from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "username",
        # "email",
        "registration_accepted",
        "is_staff",
        "is_superuser",
    )

    def get_fieldsets(self, request, obj=None):
        """
        Override `get_fieldsets()` to add `registration_accepted` to a `Moderator Permissions` section of `CustomUser` change view.
        """
        # Get the default `fieldsets` from the superclass `UserAdmin`:
        fieldsets = super().get_fieldsets(request, obj)

        # Convert fieldsets to list:
        fieldsets_as_list = list(fieldsets)

        # Create list of single tuple for `registration_accepted`:
        moderator_permissions_as_list = [
            ("Moderator Permissions", {"fields": ("registration_accepted",)})
        ]

        # Combine the two lists and return the result:
        return moderator_permissions_as_list + fieldsets_as_list
