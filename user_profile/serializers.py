from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)
    is_plus = serializers.SerializerMethodField()

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
            'is_plus',
            'referral_code'
        ]

    def get_is_plus(self, obj):
        subscription = getattr(obj.user, 'subscription', None)
        return bool(
            subscription and
            subscription.is_active and
            subscription.expires_at > timezone.now()
        )