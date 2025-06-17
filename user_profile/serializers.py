from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)
    subscription_type = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'username',
            'email',
            'language',
            'currency',
            'dark_mode',
            'notifications_enabled',
            'face_id_enabled',
            'date_joined',
            'subscription_type',
            'referral_code'
        ]

    def get_subscription_type(self, obj):
        sub = getattr(obj.user, 'subscription', None)
        if sub and sub.is_active and sub.expires_at > timezone.now():
            return sub.type
        return None