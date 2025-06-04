from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

from .models import UserSubscription


class SubscriptionsApiTests(APITestCase):
    def setUp(self):
        """Авторизуем тестового пользователя"""
        self.user = User.objects.create_user(username="test", password="pass")
        self.client.force_authenticate(user=self.user)

    def test_activate_subscription(self):
        """Активация подписки для пользователя"""
        url = reverse("activate_subscription")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(UserSubscription.objects.filter(user=self.user).exists())

    def test_get_subscription(self):
        """Получение активной подписки"""
        expires = timezone.now() + timedelta(days=30)
        UserSubscription.objects.create(
            user=self.user,
            plan="monthly",
            source="admin",
            expires_at=expires,
            is_active=True,
        )
        url = reverse("user_subscription")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["plan"], "monthly")

