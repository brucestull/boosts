from django.urls import path

from . import views


app_name = 'boosts'

urlpatterns = [
    path('', views.StatementListView.as_view(), name='statement-list'),
]