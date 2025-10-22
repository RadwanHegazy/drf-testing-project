from rest_framework.test import APITestCase
from django.urls import reverse
from globals.test_objects import create_user, create_jwt_headers, create_category


class TestCreateProduct (APITestCase) : 

    def setUp(self):
        self.endpoint = reverse('create-product')

    def test_unauhtorized(self):
        res = self.client.post(self.endpoint)
        self.assertEqual(res.status_code, 401)

    def test_success(self):
        user = create_user(username='testuser')
        headers = create_jwt_headers(user)
        data = {
            'title' : "Laptop",
            'body' : "test body",
            'category' : create_category().id,
            'price' : 1000,
            'quantity' : 10,
            'test_field' : "test value",
        }
        res = self.client.post(self.endpoint, data, headers=headers)
        self.assertEqual(res.status_code, 201)
    
    def test_no_body(self):
        user = create_user(username='testuser')
        headers = create_jwt_headers(user)
        res = self.client.post(self.endpoint, headers=headers)
        self.assertEqual(res.status_code, 400)
    