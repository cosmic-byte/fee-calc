"""fee_calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Loan Application Fee Calculator Web Service Documentation",
        default_version="v1.0",
        description="An api that returns a fee based on the loan application figures.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support.fee_calculator.com"),
        license=openapi.License(name="Fee Calculator License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/admin", admin.site.urls),
    path("api/auth", include("fee_calculator.apps.user.urls")),
    path("api/core", include("fee_calculator.apps.core.urls")),
]
