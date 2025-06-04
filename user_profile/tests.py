from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfileApiTests(APITestCase):
    def setUp(self):
        """Создаем и авторизуем пользователя"""
        self.user = User.objects.create_user(
            username="user", email="user@example.com", password="pass"
        )
        self.client.force_authenticate(user=self.user)

    def test_get_profile(self):
        """Получение профиля текущего пользователя"""
        url = reverse("profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "user")

    def test_update_profile(self):
        """Изменение настроек профиля"""
        url = reverse("profile")
        response = self.client.patch(url, {"dark_mode": True}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["dark_mode"])

    def test_pin_create_and_verify(self):
        """Создание PIN-кода и его проверка"""
        create_url = reverse("pin_create")
        self.client.post(create_url, {"pin": "1234"}, format="json")
        verify_url = reverse("pin_verify")
        response = self.client.post(verify_url, {"pin": "1234"}, format="json")
        self.assertTrue(response.data["valid"])
        wrong = self.client.post(verify_url, {"pin": "0000"}, format="json")
        self.assertFalse(wrong.data["valid"])

    def test_delete_profile(self):
        """Удаление профиля пользователя"""
        url = "/api/profile/profile/delete/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
