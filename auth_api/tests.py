from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class AuthApiTests(APITestCase):
    # Создание тестового пользователя
    def setUp(self):
        self.existing_user = User.objects.create_user(
            username="existinguser",
            email="exist@example.com",
            password="StrongPass123"
        )

    # Проверка на успех регистрации
    def test_register_success(self):
        url = reverse('register')
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    # Проверка на дублирование username пользователей
    def test_register_duplicate_username(self):
        url = reverse('register')
        data = {
            "username": "existinguser",
            "email": "newemail@example.com",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    # Проверка на дублирование email пользователей
    def test_register_duplicate_email(self):
        url = reverse('register')
        data = {
            "username": "anotheruser",
            "email": "exist@example.com",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    # Проверка на валидность пароля при регистрации
    def test_register_invalid_password(self):
        url = reverse('register')
        data = {
            "username": "userbadpass",
            "email": "userbadpass@example.com",
            "password": "123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    # Проверка на отсутствие ввода username
    def test_register_missing_username_field(self):
        url = reverse('register')
        data = {
            "email": "missingfields@example.com",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    # Проверка на отсутствие ввода email
    def test_register_missing_email_field(self):
        url = reverse('register')
        data = {
            "username": "usermissemail",
            "password": "StrongPass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    # Проверка на отсутствие ввода password
    def test_register_missing_password_field(self):
        url = reverse('register')
        data = {
            "username": "usermisspass",
            "email": "missingfields@example.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)