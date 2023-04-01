from django.urls import path

from . import views


app_name = "boosts"

urlpatterns = [
    path(
        "inspirationals/",
        views.InspirationalListView.as_view(),
        name="inspirational-list",
    ),
    path(
        "create/",
        views.InspirationalCreateView.as_view(),
        name="inspirational-create",
    ),
]
