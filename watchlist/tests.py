from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

from stocks.models import Stock
from .models import WatchedStock


class WatchlistApiTests(APITestCase):
    def setUp(self):
        """Создание пользователя и тестовой акции"""
        self.user = User.objects.create_user(username="test", password="pass")
        self.stock = Stock.objects.create(
            name="Apple",
            ticker="AAPL",
            exchange="NASDAQ",
            country="USA",
            current_price=100,
            currency="USD",
        )
        self.client.force_authenticate(user=self.user)

    def test_add_stock_to_watchlist(self):
        """Добавление акции в список наблюдения"""
        url = reverse("watchlist-list")
        data = {"stock": self.stock.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(WatchedStock.objects.filter(user=self.user, stock=self.stock).exists())

    def test_add_duplicate_stock(self):
        """Проверяем, что дубликаты не добавляются"""
        WatchedStock.objects.create(user=self.user, stock=self.stock)
        url = reverse("watchlist-list")
        data = {"stock": self.stock.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_stock_by_action(self):
        """Удаляем акцию по её id через спец. эндпоинт"""
        WatchedStock.objects.create(user=self.user, stock=self.stock)
        url = f"/api/watchlist/stock/{self.stock.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

