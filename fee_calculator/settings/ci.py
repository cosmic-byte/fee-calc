from fee_calculator.settings.dev import *  # NOQA (ignore all errors on this line)

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY", "alq7#8r33k!cv47r8pelqldnkl46v!b4-sfwvdo$x(=p%1read"
)
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "testdb"}}
