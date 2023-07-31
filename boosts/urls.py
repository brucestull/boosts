from django.urls import path

from . import views

# Define the app name:
app_name = "boosts"

# Define the URL patterns for the `boosts` app:
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
    path(
        "send/<int:pk>/",
        views.send_inspirational,
        name="send-inspirational",
    ),
]
