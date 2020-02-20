import pytest
from django.urls import reverse
from rest_framework import status

from fee_calculator.apps.user.models import User
from fee_calculator.tests.test_utils import authenticate_user


class TestUserView:
    @pytest.mark.django_db
    def test_create_new_user_should_pass(self, random_email, api_client):
        url = reverse("create")
        payload = {
            "email": random_email,
            "password": "password"
        }
        response = api_client.post(url, payload, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert len(response.data) == 2

    @pytest.mark.django_db
    def test_create_new_user_with_existing_email_should_fail(self, random_email, api_client):
        url = reverse("create")
        payload = {
            "email": random_email,
            "password": "password"
        }
        response = api_client.post(url, payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED

        response = api_client.post(url, payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.django_db
    def test_enable_or_disable_user_success(self, user, api_client):
        client = authenticate_user(api_client, user)

        url = reverse("enable-disable", kwargs={"uid": str(user.uid)})
        response = client.put(url, format="json")
        assert response.status_code == status.HTTP_200_OK

        user = User.objects.get(uid=user.uid)
        assert user.is_active is False

        response = client.put(url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_delete_user_success(self, user, api_client):
        client = authenticate_user(api_client, user)

        url = reverse("delete", kwargs={"uid": str(user.uid)})
        response = client.put(url, format="json")
        assert response.status_code == status.HTTP_200_OK

        user = User.objects.get(uid=user.uid)
        assert user.deleted is True

        response = client.put(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        user = User.objects.get(uid=user.uid)
        assert user.deleted is False
