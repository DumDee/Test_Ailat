from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'language',
            'currency',
            'dark_mode',
            'notifications_enabled',
            'face_id_enabled'
        ]
