from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin

from api.serializers import CurrentUserSerializer, InspirationalSerializer
from api.permissions import IsRegistrationAccepted, IsStaff
from boosts.models import Inspirational


class CurrentUserViewSet(LoginRequiredMixin, generics.RetrieveAPIView):
    serializer_class = CurrentUserSerializer

    def get_object(self):
        return self.request.user


# class InspirationalsViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
class InspirationalsViewSet(viewsets.ModelViewSet):
    """
    View set for the Inspirational model.
    """
    permission_classes = [
        IsAuthenticated,
    #     IsRegistrationAccepted,
    #     IsStaff,
    ]
    serializer_class = InspirationalSerializer
    queryset = Inspirational.objects.all()
