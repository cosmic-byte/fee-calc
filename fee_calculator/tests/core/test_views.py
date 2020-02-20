import pytest
from django.urls import reverse
from rest_framework import status

from fee_calculator.tests.test_utils import authenticate_user
from fee_calculator.apps.core.constants import LOAN_TENURE_BI_ANNUAL


class TestLoanApplicationFeeView:
    @pytest.mark.django_db
    def test_calculate_loan_fee_success(self, user, api_client):
        client = authenticate_user(api_client, user)

        expected_response = {
           "loan_fee": 115.0
        }
        url = reverse("calculate_fee")
        payload = {
            "loan_amount": 2750,
            "tenure": LOAN_TENURE_BI_ANNUAL
        }
        response = client.post(url, payload, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response

    @pytest.mark.django_db
    def test_calculate_loan_fee_with_invalid_payload_should_fail(self, user, api_client):
        client = authenticate_user(api_client, user)

        url = reverse("calculate_fee")
        payload = {
            "loan_amount": 200_000_000,  # Value greater than 20,000
            "tenure": LOAN_TENURE_BI_ANNUAL
        }
        response = client.post(url, payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        payload = {
            "loan_amount": 2000,
            "tenure": 2  # Invalid loan tenure
        }
        response = client.post(url, payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
