from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Item, Category

class SimpleTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class ItemModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fruits")
        self.item = Item.objects.create(
            name="Apple",
            category=self.category,
            quantity_in_stock=100,
            price=0.50
        )

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Apple")
        self.assertEqual(self.item.category.name, "Fruits")
        self.assertEqual(self.item.quantity_in_stock, 100)
        self.assertEqual(float(self.item.price), 0.50)

    def test_item_quantity_cannot_be_negative(self):
        item = Item(name="Test", category=self.category, quantity_in_stock=-5, price=1.00)
        with self.assertRaises(ValidationError):
            item.full_clean()

class InventoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_inventory_page_status_code(self):
        response = self.client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)

    def test_inventory_page_template(self):
        response = self.client.get(reverse('inventory_list'))
        self.assertTemplateUsed(response, 'inventory_list.html')

    def test_inventory_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('inventory_list'))
        self.assertRedirects(response, '/login/?next=/inventory/')