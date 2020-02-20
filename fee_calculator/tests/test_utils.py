from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework.test import APIClient

from fee_calculator.apps.user.models import User


def authenticate_user(client, user, admin_user=False):
    if admin_user:
        user.is_superuser = True
        user.save()
    serializer = JSONWebTokenSerializer()
    attrs = {
        "email": user.email,
        "password": "password",
    }
    user_credential = serializer.validate(attrs)
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_credential.get("token"))
    return client


def get_authenticated_user_client():
    client = APIClient()
    User.objects.create_user(email="greg.obinna@gmail.com", password="password")
    serializer = JSONWebTokenSerializer()
    attrs = {
        "email": "greg.obinna@gmail.com",
        "password": "password",
    }
    user_credential = serializer.validate(attrs)
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_credential.get("token"))
    return client
