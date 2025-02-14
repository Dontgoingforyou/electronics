from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from electronics.models import NetworkNode


class NetworkNodeAPITestCase(APITestCase):
    def setUp(self):
        """ Создание тестового пользователя и нескольких объектов. """

        self.user = User.objects.create_user(username="admin", password="123qwe", is_staff=True)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.factory = NetworkNode.objects.create(
            name="Завод Электрон",
            email="factory@example.com",
            country="Россия",
            city="Москва",
            street="Ленина",
            house_number="10",
            debt=5000.00
        )

        self.retail = NetworkNode.objects.create(
            name="Розничная сеть",
            email="retail@example.com",
            country="Россия",
            city="Санкт-Петербург",
            street="Невский",
            house_number="25",
            supplier=self.factory,
            debt=2000.00
        )

        self.url = "/electronics/"

    def test_get_network_nodes(self):
        """ Проверка получения списка объектов. """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_network_node(self):
        """ Проверка создания нового объекта. """
        data = {
            "name": "ИП Петров",
            "email": "ip.petrov@example.com",
            "country": "Казахстан",
            "city": "Алматы",
            "street": "Абая",
            "house_number": "15",
            "supplier": self.retail.id,
            "debt": 1000.00
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NetworkNode.objects.count(), 3)

    def test_filter_by_country(self):
        """ Проверка фильтрации по стране. """

        response = self.client.get(self.url, {"country": "Россия"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_debt_field_is_readonly(self):
        """ Проверка, что поле 'debt' нельзя обновить через API. """

        response = self.client.patch(f"{self.url}{self.retail.id}/", {"debt": 0}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.retail.refresh_from_db()
        self.assertNotEqual(self.retail.debt, 0)

    def test_delete_network_node(self):
        """ Проверка удаления объекта. """

        response = self.client.delete(f"{self.url}{self.retail.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(NetworkNode.objects.count(), 1)
