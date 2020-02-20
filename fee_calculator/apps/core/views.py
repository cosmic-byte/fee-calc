from rest_framework import status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from fee_calculator.apps.core.serializer import LoanApplicationSerializer
from fee_calculator.apps.user.models import User


class LoanApplicationFeeView(CreateAPIView):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = LoanApplicationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Process Loan Fee view.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            loan_application = serializer.create(serializer.validated_data)
            read_serializer = self.serializer_class(loan_application)
            return Response(read_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
