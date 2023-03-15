from django.contrib import admin

from boosts.models import Inspirational


@admin.register(Inspirational)
class InspirationalAdmin(admin.ModelAdmin):
    list_display = (
        'body',
        'author',
        'created',
    )
