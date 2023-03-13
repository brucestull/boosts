from django.contrib import admin

from boosts.models import Statement


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = (
        'body',
        'author',
        'created',
    )
