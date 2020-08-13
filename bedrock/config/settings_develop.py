import os
from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get(
            "SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")
        ),
        "USER": os.environ.get("SQL_USER", ""),
        "PASSWORD": os.environ.get("SQL_PASSWORD", ""),
        "HOST": os.environ.get("SQL_HOST", ""),
        "PORT": os.environ.get("SQL_PORT", ""),
    }
}

# Installed App

INSTALLED_APPS += [
    "django_extensions",
]

# Jupyter Notebook Arguments

NOTEBOOK_ARGUMENTS = [
    "--ip",
    "0.0.0.0",
    "--allow-root",
    "--no-browser",
    "--NotebookApp.disable_check_xsrf=True",
    "--NotebookApp.token=''",
    "--NotebookApp.password=''",
    "--NotebookApp.iopub_data_rate_limit=10000000000",
]
