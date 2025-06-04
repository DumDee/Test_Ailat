from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .models import Partner, Product, IssueReport


class OffersApiTests(APITestCase):
    def setUp(self):
        """Создаем тестового партнера и продукт"""
        self.partner = Partner.objects.create(name="Partner", description="Desc")
        self.product = Product.objects.create(
            partner=self.partner,
            name="Prod1",
            description="Desc",
            product_type="Wakala",
        )

    def test_list_partners(self):
        """Проверяем получение списка партнеров"""
        url = reverse("partners-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Partner")

    def test_list_products(self):
        """Проверяем получение списка продуктов"""
        url = reverse("products-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Prod1")

    def test_create_issue_report(self):
        """Отправляем жалобу на продукт"""
        url = reverse("issues-list")
        data = {"product": self.product.id, "description": "Problem"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(IssueReport.objects.filter(product=self.product).exists())

