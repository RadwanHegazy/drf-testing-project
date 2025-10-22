from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TestUserLogin(APITestCase) : 

    def setUp(self):
        self.endpoint = reverse('token_obtain_pair')

    def test_username_not_exists(self) :
        data = {
            'username' : "test",
            'password' : "testpassword123",
        }

        res = self.client.post(self.endpoint, data)
        self.assertEqual(res.status_code, 401)

    def test_incorrect_password(self) :
        user = User.objects.create_user(
            username="test",
            password="123"
        )

        data = {
            'username' : 'test',
            'password' : '1234'
        }

        res = self.client.post(self.endpoint, data)
        self.assertEqual(res.status_code, 401)


    def test_successful_login(self) :
        user = User.objects.create_user(
            username="test",
            password="123"
        )

        data = {
            'username' : user.username,
            'password' : '123'
        }

        res = self.client.post(self.endpoint, data)
        self.assertEqual(res.status_code, 200)
