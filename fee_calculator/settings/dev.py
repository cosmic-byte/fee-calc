import sys
from fee_calculator.settings.base import *  # NOQA (ignore all errors on this line)

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY", "alq7#8r33k!cv47r8pelqldnkl46v!b4-sfwvdo$x(=p%1read"
)
JWT_AUTH.update({"JWT_SECRET_KEY": SECRET_KEY})
DEBUG = os.getenv("DJANGO_DEBUG", True)

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")
BASE_URL = "http://127.0.0.1:8000"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DATABASE_NAME", "fee_calculator"),
        "USER": os.getenv("DATABASE_USER", "fee_calculator"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "fee_calculator"),
        "HOST": os.getenv("DATABASE_HOST", "calculator_db"),
        "PORT": os.getenv("DATABASE_PORT", 5432),
        "ATOMIC_REQUESTS": True,
    }
}

if "test" in sys.argv:
    DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3", "NAME": "testdb"}
