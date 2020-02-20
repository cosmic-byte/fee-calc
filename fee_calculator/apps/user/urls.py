from django.urls import path

from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

from fee_calculator.apps.user.views import (
    UserCreateView,
    EnableOrDisableUser,
    DeleteUserView,
)
from fee_calculator.auth import JWTSerializer, JWTRefreshTokenSerializer

urlpatterns = [
    path("/create", UserCreateView.as_view(), name="create"),
    path("/<uuid:uid>/delete", DeleteUserView.as_view(), name="delete"),
    path(
        "/<uuid:uid>/enable-disable",
        EnableOrDisableUser.as_view(),
        name="enable-disable",
    ),
    path(
        "/login",
        ObtainJSONWebToken.as_view(serializer_class=JWTSerializer),
        name="login",
    ),
    path(
        "/api-token-refresh",
        RefreshJSONWebToken.as_view(serializer_class=JWTRefreshTokenSerializer),
        name="refresh",
    ),
]
