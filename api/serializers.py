from rest_framework import serializers
from django.contrib.auth import get_user_model

from boosts.models import Inspirational


class NestedStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inspirational
        fields = [
            'id',
            'body',
        ]


class CurrentUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the current user.
    """

    statements_detail = NestedStatementSerializer(
        source='inspirationals',
        many=True,
        read_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'statements_detail',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
        }
            
            