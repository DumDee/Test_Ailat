from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import UserSubscription
from .serializers import UserSubscriptionSerializer
from django.utils import timezone
from datetime import timedelta


class UserSubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            subscription = request.user.subscription
            serializer = UserSubscriptionSerializer(subscription)
            return Response(serializer.data)
        except UserSubscription.DoesNotExist:
            return Response({'detail': 'Нет активной подписки'}, status=404)


class ActivateSubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        expires = timezone.now() + timedelta(days=30)
        subscription, created = UserSubscription.objects.update_or_create(
            user=request.user,
            defaults={
                'plan': 'monthly',
                'source': 'admin',
                'is_active': True,
                'activated_at': timezone.now(),
                'expires_at': expires
            }
        )
        return Response({'detail': 'Подписка активирована'}, status=200)
