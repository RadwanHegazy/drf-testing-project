from django.contrib.auth import get_user_model
from uuid import uuid4
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

def create_user(
    username = None,
    email = 'test@gmail.com',
    password = '123',
    is_superuser = False
) : 
    return User.objects.create_user(
        username = username or str(uuid4()),
        email = email,
        password = password,
        is_superuser = is_superuser
    )


def create_access_token(user=None) : 
    return str(AccessToken.for_user(user or create_user()))

def create_jwt_headers(user=None) : 
    user = user or create_user()
    return {
        'Authorization' : f'Bearer {create_access_token(user)}'
    }