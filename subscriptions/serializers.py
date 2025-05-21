from rest_framework import serializers
from .models import UserSubscription


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = [
            'plan',
            'source',
            'is_active',
            'activated_at',
            'expires_at'
        ]
