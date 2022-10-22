from api_core.settings.base import *
from os import environ

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "OPTIONS": {
            "NAME": environ.get("DB_NAME"),
            "USER": environ.get("DB_USER"),
            "PASSWORD": environ.get("DB_PASSWORD"),
            "HOST": "db",
            "PORT": "5432",
        },
    }
}
