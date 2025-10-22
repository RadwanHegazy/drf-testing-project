from rest_framework.test import APITestCase
from django.urls import reverse
from globals.test_objects import create_user, create_product, create_category


class TestListProducts (APITestCase) : 

    def setUp(self):
        self.endpoint = reverse('list-product')

    def test_list_products(self):
        res = self.client.get(self.endpoint)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 0)

    def test_list_products_with_data(self):
        user = create_user(username='radwan')
        category = create_category(name='Electronics')
        
        create_product(category=category)
        create_product(category=category)

        res = self.client.get(self.endpoint)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 2)

    def test_list_products_no_available_quantity(self):
        user = create_user()
        category = create_category()
        
        create_product(category=category, quantity=0)

        res = self.client.get(self.endpoint)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 0)