from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .models import Stock


class StocksApiTests(APITestCase):
    # Создание тестовых данных
    def setUp(self):
        self.stock = Stock.objects.create(
            name="Apple",
            ticker="AAPL",
            exchange="NASDAQ",
            country="USA",
            current_price=100,
            currency="USD",
            is_free_access=True,
        )

    # Проверка получения списка акций
    def test_list_stocks(self):
        url = reverse("stocks-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["ticker"], "AAPL")

    # Проверка получения конкретной акции
    def test_retrieve_stock(self):
        url = reverse("stocks-detail", args=[self.stock.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ticker"], "AAPL")