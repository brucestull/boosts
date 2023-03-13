from rest_framework import serializers
from django.contrib.auth import get_user_model

from boosts.models import Statement


class NestedStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statement
        fields = [
            'id',
            'body',
        ]


class CurrentUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the current user.
    """

    statements_detail = NestedStatementSerializer(
        source='statements',
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
            
            