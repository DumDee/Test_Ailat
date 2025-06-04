from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .models import Stock


class StocksApiTests(APITestCase):
    def setUp(self):
        """Создаем тестовую акцию"""
        self.stock = Stock.objects.create(
            name="Apple",
            ticker="AAPL",
            exchange="NASDAQ",
            country="USA",
            current_price=100,
            currency="USD",
        )

    def test_list_stocks(self):
        """Проверяем получение списка акций"""
        url = reverse("stocks-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["ticker"], "AAPL")

    def test_retrieve_stock(self):
        """Проверяем получение конкретной акции"""
        url = reverse("stocks-detail", args=[self.stock.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ticker"], "AAPL")

