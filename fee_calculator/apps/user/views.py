from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from fee_calculator.apps.user.serializer import (
    UserCreateSerializer,
    EnableDisableUserSerializer,
    DeleteUserSerializer,
)
from fee_calculator.permissions import CustomDjangoModelPermissions

User = get_user_model()


class UserCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.data)
        payload = jwt_payload_handler(user)
        response = {"token": jwt_encode_handler(payload), "user": serializer.data}
        return Response(response, status=status.HTTP_201_CREATED)


class EnableOrDisableUser(UpdateAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    queryset = User.objects.all()
    serializer_class = EnableDisableUserSerializer
    lookup_field = "uid"


class DeleteUserView(UpdateAPIView):
    permission_classes = (CustomDjangoModelPermissions,)
    queryset = User.objects.all()
    serializer_class = DeleteUserSerializer
    lookup_field = "uid"
