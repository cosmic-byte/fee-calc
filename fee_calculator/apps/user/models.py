import uuid

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from fee_calculator.apps.user.manager import UserManager


class User(PermissionsMixin, AbstractBaseUser):
    GENDER_MALE = 0
    GENDER_FEMALE = 1

    GENDER = [(GENDER_MALE, "MALE"), (GENDER_FEMALE, "FEMALE")]

    uid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="Public identifier",
    )
    email = models.EmailField(max_length=100, unique=True)
    email_verified = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name_plural = "users"

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
