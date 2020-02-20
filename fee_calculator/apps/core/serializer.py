from rest_framework import serializers

from fee_calculator.apps.core import constants
from fee_calculator.apps.core.calculator import FeeCalculator, LoanApplication


class LoanApplicationSerializer(serializers.Serializer):
    tenure = serializers.ChoiceField(
        choices=constants.LOAN_TENURE,
        write_only=True
    )
    loan_amount = serializers.FloatField(
        min_value=constants.MINIMUM_LOAN_AMOUNT,
        max_value=constants.MAXIMUM_LOAN_AMOUNT,
        write_only=True
    )
    loan_fee = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        loan_application = LoanApplication(**validated_data)
        calculator = FeeCalculator(loan_application)
        loan_application.loan_fee = calculator.calculate()
        return loan_application

