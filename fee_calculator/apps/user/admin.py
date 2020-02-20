from django.contrib import admin

# Register your models here.
from fee_calculator.apps.user import models

admin.site.register(models.User)
