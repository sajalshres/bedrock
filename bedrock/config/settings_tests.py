from .settings import *

SECRET_KEY = "0*t8wbjz%^+^pbvtfo6=j75bep0ynyd$=s1@2aqot-os6_tbqt"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}
