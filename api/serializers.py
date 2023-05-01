from rest_framework import serializers
from django.contrib.auth import get_user_model

from boosts.models import Inspirational


class InspirationalSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Inspirational
            fields = [
                'id',
                'body',
                'author',
                'created',
            ]
            # extra_kwargs = {
            #     'id': {'read_only': True},
            #     'author': {'read_only': True},
            #     'created': {'read_only': True},
            # }


class NestedInspirationalSerializer(serializers.ModelSerializer):

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

    inspirationals_detail = NestedInspirationalSerializer(
        source='inspirationals',
        many=True,
        read_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'inspirationals_detail',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
        }
            
            