from rest_framework import serializers
from .models import Referral

class ReferralSerializer(serializers.ModelSerializer):
    # referrer_username = serializers.CharField(source='referrer.username', read_only=True)
    referred_username = serializers.CharField(source='referred.username', read_only=True)
    referred_id = serializers.IntegerField(source='referred.id', read_only=True)

    # class Meta:
    #     model = Referral
    #     fields = ['id', 'referrer', 'referrer_username', 'referred', 'referred_username', 'created_at']
    #     read_only_fields = ['id', 'referrer_username', 'referred_username', 'created_at']

    class Meta:
        model = Referral
        fields = ['id', 'referred_id', 'referred_username', 'created_at']