from rest_framework import viewsets
from rest_framework import generics

from django.contrib.auth.mixins import LoginRequiredMixin

from api.serializers import CurrentUserSerializer


class CurrentUserViewSet(LoginRequiredMixin, generics.RetrieveAPIView):
    serializer_class = CurrentUserSerializer

    def get_object(self):
        return self.request.user
