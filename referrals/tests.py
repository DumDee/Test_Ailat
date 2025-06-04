from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Referral


class ReferralsApiTests(APITestCase):
    def setUp(self):
        """Создаем пользователя и его рефералов"""
        self.referrer = User.objects.create_user(username="ref", password="pass")
        self.referred1 = User.objects.create_user(username="r1", password="pass")
        self.referred2 = User.objects.create_user(username="r2", password="pass")
        Referral.objects.create(referrer=self.referrer, referred=self.referred1)
        Referral.objects.create(referrer=self.referrer, referred=self.referred2)
        self.client.force_authenticate(user=self.referrer)

    def test_list_referrals(self):
        """Получение списка приглашенных пользователей"""
        url = reverse("my-referrals")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

