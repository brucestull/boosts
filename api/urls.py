from django.urls import path

from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()

urlpatterns = router.urls + [
    path('current-user/', views.CurrentUserViewSet.as_view(), name='current-user')
]
