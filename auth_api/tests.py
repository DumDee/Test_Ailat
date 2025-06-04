from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class AuthApiTests(APITestCase):
    def setUp(self):
        """Создание пользователя для проверки дубликатов"""
        self.existing_user = User.objects.create_user(
            username="existinguser",
            email="exist@example.com",
            password="StrongPass123"
        )

    def test_register_success(self):
        """Регистрация нового пользователя с корректными данными"""
        url = reverse('register')
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_register_duplicate_username(self):
        """Попытка регистрации с уже занятым username"""
        url = reverse('register')
        data = {
            "username": "existinguser",
            "email": "newemail@example.com",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_register_duplicate_email(self):
        """Попытка регистрации с уже существующим email"""
        url = reverse('register')
        data = {
            "username": "anotheruser",
            "email": "exist@example.com",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_register_invalid_password(self):
        """Регистрация с простым или слишком коротким паролем"""
        url = reverse('register')
        data = {
            "username": "userbadpass",
            "email": "userbadpass@example.com",
            "password": "123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_register_missing_username_field(self):
        """Проверка ответа при отсутствии поля username"""
        url = reverse('register')
        data = {
            "email": "missingfields@example.com",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_register_missing_email_field(self):
        """Проверка ответа при отсутствии поля email"""
        url = reverse('register')
        data = {
            "username": "usermissemail",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_register_missing_password_field(self):
        """Проверка ответа при отсутствии поля password"""
        url = reverse('register')
        data = {
            "username": "usermisspass",
            "email": "missingfields@example.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
