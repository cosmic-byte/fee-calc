from random import random, randint

import pytest

from rest_framework.test import APIClient

from fee_calculator.apps.core.calculator import LoanApplication
from fee_calculator.apps.core.constants import LOAN_TENURE_ANNUAL
from fee_calculator.tests.user.factories import UserFactory


@pytest.fixture
def random_email():
    return "email{}@email.com".format(random())


@pytest.fixture
def random_id(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


@pytest.fixture
def user():
    # Make every user an admin to avoid permission issues while testing
    return UserFactory(is_admin=True, is_superuser=True)


@pytest.fixture
def loan_application():
    return LoanApplication(tenure=LOAN_TENURE_ANNUAL, loan_amount=2750)


@pytest.fixture
def api_client():
    return APIClient()

