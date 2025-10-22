from rest_framework.test import APITestCase
from django.urls import reverse
from globals.test_objects import create_user, create_category


class TestListCategory (APITestCase) : 

    def setUp(self):
        self.endpoint = reverse('list-category')

    def test_list_category(self):
        res = self.client.get(self.endpoint)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 0)

    def test_list_category_with_data(self):
        user = create_user(username='radwan')
        category = create_category(name='Electronics')

        res = self.client.get(self.endpoint)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)
