from django.urls import path

from fee_calculator.apps.core.views import LoanApplicationFeeView

urlpatterns = [path("/calculate-fee", LoanApplicationFeeView.as_view(), name="calculate_fee")]
