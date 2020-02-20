from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_base_user(self, email=None, password=None, **extra_fields):
        if not email or not password:
            raise ValueError("The email and password must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_base_user(email=email, password=password, **extra_fields)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
