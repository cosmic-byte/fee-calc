from fee_calculator.apps.core.calculator import FeeCalculator
from fee_calculator.apps.core.constants import *


class TestFeeCalculator:

    def test_calculate(self, loan_application):
        fee_calculator = FeeCalculator(loan_application)
        result = fee_calculator.calculate()
        assert result == 90.0

    def test_get_loan_boundaries(self, loan_application):
        fee_calculator = FeeCalculator(loan_application)
        expected_result = (2000, 3000)
        result = fee_calculator._get_loan_boundaries()  # Accessing private method for testing purpose
        assert result == expected_result

    def test_get_loan_boundaries_for_minimum_amount(self, loan_application):
        loan_application.loan_amount = MINIMUM_LOAN_AMOUNT
        fee_calculator = FeeCalculator(loan_application)
        expected_result = (MINIMUM_LOAN_AMOUNT, MINIMUM_LOAN_AMOUNT)
        result = fee_calculator._get_loan_boundaries()  # Accessing private method for testing purpose
        assert result == expected_result

    def test_get_loan_boundaries_for_maximum_amount(self, loan_application):
        loan_application.loan_amount = MAXIMUM_LOAN_AMOUNT
        fee_calculator = FeeCalculator(loan_application)
        expected_result = (MAXIMUM_LOAN_AMOUNT, MAXIMUM_LOAN_AMOUNT)
        result = fee_calculator._get_loan_boundaries()  # Accessing private method for testing purpose
        assert result == expected_result

    def test_round_down_loan_fee(self, loan_application):
        loan_application.loan_amount = 2000.45
        mock_fee = 51.32
        expected_fee = 49.55
        fee_calculator = FeeCalculator(loan_application)
        result = fee_calculator._round_loan_fee(mock_fee)  # Accessing private method for testing purpose
        assert result == expected_fee

    def test_round_up_loan_fee(self, loan_application):
        loan_application.loan_amount = 2002.45
        mock_fee = 51.32
        expected_fee = 52.55
        fee_calculator = FeeCalculator(loan_application)
        result = fee_calculator._round_loan_fee(mock_fee)  # Accessing private method for testing purpose
        assert result == expected_fee
