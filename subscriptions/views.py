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
        data = request.data
        plan = data.get('plan', 'monthly')
        source = data.get('source', 'admin')
        sub_type = data.get('type', 'pro')
        duration = int(data.get('duration_days', 30))

        expires = timezone.now() + timedelta(days=duration)

        subscription, created = UserSubscription.objects.update_or_create(
            user=request.user,
            defaults={
                'plan': plan,
                'source': source,
                'type': sub_type,
                'is_active': True,
                'activated_at': timezone.now(),
                'expires_at': expires
            }
        )
        return Response({'detail': 'Подписка активирована'}, status=200)
