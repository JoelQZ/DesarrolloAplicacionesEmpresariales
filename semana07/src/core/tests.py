from django.test import TestCase

from .models import Item


class ItemListViewTests(TestCase):
	def test_item_list_displays_items(self):
		item = Item.objects.create(name="Laptop", description="Equipo portatil")

		response = self.client.get("/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, item.name)
		self.assertContains(response, item.description)

	def test_item_list_displays_empty_message(self):
		response = self.client.get("/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No existen items registrados.")
