from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class UserProfileApiTests(APITestCase):
    # Создание и авторизация тестовых данных
    def setUp(self):
        self.user = User.objects.create_user(
            username="user", email="user@example.com", password="pass"
        )
        self.client.force_authenticate(user=self.user)

    # Тест на получение профиля текущего пользователя
    def test_get_profile(self):
        url = reverse("profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "user")

    # Тест изменения настроек профиля
    def test_update_profile(self):
        url = reverse("profile")
        response = self.client.patch(url, {"dark_mode": True}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["dark_mode"])

    # Тест на создание и проверку PIN-кода
    def test_pin_create_and_verify(self):
        create_url = reverse("pin_create")
        self.client.post(create_url, {"pin": "1234"}, format="json")
        verify_url = reverse("pin_verify")
        response = self.client.post(verify_url, {"pin": "1234"}, format="json")
        self.assertTrue(response.data["valid"])
        wrong = self.client.post(verify_url, {"pin": "0000"}, format="json")
        self.assertFalse(wrong.data["valid"])

    # Проверка удаления профиля пользователя
    def test_delete_profile(self):
        url = "/api/profile/profile/delete/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)