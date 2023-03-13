from django.urls import path

from . import views


app_name = "boosts"

urlpatterns = [
    path("statements/", views.StatementListView.as_view(), name="statement-list"),
    path("create/", views.StatementCreateView.as_view(), name="statement-create"),
]
