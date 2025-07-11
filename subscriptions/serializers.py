from rest_framework import serializers
from .models import UserSubscription

class ActivateSubscriptionSerializer(serializers.Serializer):
    plan = serializers.ChoiceField(choices=['monthly', 'yearly'], default='monthly')
    source = serializers.ChoiceField(choices=['apple', 'card', 'kaspi', 'admin'])
    type = serializers.ChoiceField(choices=['pro', 'plus'])

class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = [
            'plan',
            'source',
            'type',
            'is_active',
            'activated_at',
            'expires_at'
        ]
