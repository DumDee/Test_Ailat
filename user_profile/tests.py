from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
import logging

logging.disable(logging.CRITICAL)

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


# Негативные тесты проверки ПИН-кода
class PinNegativeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="StrongPass123")
        self.client.force_authenticate(user=self.user)
        self.url_create = reverse("pin_create")
        self.url_verify = reverse("pin_verify")

    def test_create_pin_too_short(self):
        data = {"pin": "123"}
        response = self.client.post(self.url_create, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("pin", response.data)

    def test_create_pin_invalid_chars(self):
        data = {"pin": "12ab"}
        response = self.client.post(self.url_create, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("pin", response.data)

    def test_create_pin_missing(self):
        data = {}
        response = self.client.post(self.url_create, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("pin", response.data)

    def test_verify_pin_missing(self):
        data = {}
        response = self.client.post(self.url_verify, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("pin", response.data)

    def test_throttling_exceeded(self):
        data = {"pin": "1234"}
        for _ in range(5):
            response = self.client.post(self.url_verify, data, format="json")
            # допустим, первые 5 запросов проходят
            self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_400_BAD_REQUEST])
        # шестой запрос должен быть заблокирован
        response = self.client.post(self.url_verify, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
