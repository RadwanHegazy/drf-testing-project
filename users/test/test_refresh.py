from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class TestTokenRefresh(APITestCase) :

    def setUp(self):
        self.endpoint = reverse('token_refresh')

    def test_invalid_token(self) :
        data = {
            'refresh' : "test"
        }

        req = self.client.post(self.endpoint, data)
        self.assertEqual(req.status_code, 401)

    def test_successful_token_refresh(self) :
        user = User.objects.create_user(
            username="test",
            password="123"
        )

        refresh_data = {
            'refresh' : str(RefreshToken.for_user(user))
        }

        refresh_res = self.client.post(self.endpoint, refresh_data)
        self.assertEqual(refresh_res.status_code, 200)