from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.serializers import CurrentUserSerializer, InspirationalSerializer
from api.permissions import IsRegistrationAccepted, IsStaff

from boosts.models import Inspirational


class CurrentUserViewSet(generics.RetrieveAPIView):
    serializer_class = CurrentUserSerializer

    permission_classes = [
        IsAuthenticated,
        IsRegistrationAccepted,
        IsStaff,
    ]

    def get_object(self):
        return self.request.user


class InspirationalsViewSet(viewsets.ModelViewSet):
    """
    View set for the Inspirational model.
    """

    permission_classes = [
        IsAuthenticated,
        IsRegistrationAccepted,
        IsStaff,
    ]
    serializer_class = InspirationalSerializer
    queryset = Inspirational.objects.all()
