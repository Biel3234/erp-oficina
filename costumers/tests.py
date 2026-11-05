from django.test import TestCase
from rest_framework.test import APIClient

from .models import Costumer, Motorcycle


class MotorcycleDeleteUpdateTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.owner = Costumer.objects.create(name="Cliente", phone="11999999999")
        self.motorcycle = Motorcycle.objects.create(
            model="Honda CG",
            color="Vermelha",
            license_plate="ABC1234",
            owner=self.owner,
        )
        self.url = f"/api/costumers/motorcycles/{self.motorcycle.pk}"

    def test_get_returns_motorcycle(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.motorcycle.pk)
        self.assertEqual(response.data["model"], "Honda CG")

    def test_put_updates_motorcycle(self):
        response = self.client.put(
            self.url,
            {"model": "Honda Biz", "color": "Preta", "license_plate": "DEF5678"},
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.motorcycle.refresh_from_db()
        self.assertEqual(self.motorcycle.model, "Honda Biz")
        self.assertEqual(self.motorcycle.color, "Preta")
        self.assertEqual(self.motorcycle.license_plate, "DEF5678")

    def test_delete_removes_motorcycle(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Motorcycle.objects.filter(pk=self.motorcycle.pk).exists())
