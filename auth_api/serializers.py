from django.contrib.auth.models import User
from rest_framework import serializers
from referrals.models import Referral
from user_profile.models import Profile  # если профиль в отдельном приложении

class NullableUUIDField(serializers.Field):
    def to_internal_value(self, data):
        if not data:
            return None
        try:
            import uuid
            return uuid.UUID(str(data))
        except (ValueError, AttributeError):
            raise serializers.ValidationError('Invalid UUID format.')

    def to_representation(self, value):
        return str(value) if value else None


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    referral_code = NullableUUIDField(required=False, allow_null=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'referral_code']

    def create(self, validated_data):
        referral_code = validated_data.pop('referral_code', None)
        user = User.objects.create_user(**validated_data)
        if referral_code:
            try:
                referrer_profile = Profile.objects.get(referral_code=referral_code)
                Referral.objects.create(referrer=referrer_profile.user, referred=user)
            except Profile.DoesNotExist:
                pass  # Можно добавить логирование или ошибку
        return user
