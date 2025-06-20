from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import UserSubscription
from .serializers import UserSubscriptionSerializer, ActivateSubscriptionSerializer
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
        serializer = ActivateSubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        expires = timezone.now() + timedelta(days=data['duration_days'])

        subscription, created = UserSubscription.objects.update_or_create(
            user=request.user,
            defaults={
                'plan': data['plan'],
                'source': data['source'],
                'type': data['type'],
                'is_active': True,
                'activated_at': timezone.now(),
                'expires_at': expires
            }
        )
        return Response({'detail': 'Подписка активирована'}, status=200)
