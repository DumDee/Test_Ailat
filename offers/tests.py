from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .models import Partner, Product, IssueReport


class OffersApiTests(APITestCase):
    #Создание тестовых данных
    def setUp(self):
        self.partner = Partner.objects.create(name="Partner", description="Desc")
        self.product = Product.objects.create(
            partner=self.partner,
            name="Prod1",
            description="Desc",
            product_type="Wakala",
        )
    # Проверка получения списка партнеров
    def test_list_partners(self):
        url = reverse("partners-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Partner")

    #Проверка получения списка продуктов
    def test_list_products(self):
        url = reverse("products-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Prod1")

    #Тест создания жалобы на продукт
    def test_create_issue_report(self):
        url = reverse("issues-list")
        data = {"product": self.product.id, "description": "Problem"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(IssueReport.objects.filter(product=self.product).exists())