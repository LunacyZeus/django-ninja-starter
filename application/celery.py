import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")

from celery import Celery, platforms
from django.conf import settings

app = Celery("application")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
platforms.C_FORCE_ROOT = True
app.autodiscover_tasks()
