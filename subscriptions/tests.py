from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

from .models import UserSubscription


class SubscriptionsApiTests(APITestCase):
    # Создание и авторизация тестового пользователя
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="pass")
        self.client.force_authenticate(user=self.user)

    # Проверка активации подписки для пользователя
    def test_activate_subscription(self):
        url = reverse("activate_subscription")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(UserSubscription.objects.filter(user=self.user).exists())

    # Проверка получения активной подписки
    def test_get_subscription(self):
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
