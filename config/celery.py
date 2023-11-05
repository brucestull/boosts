import os

import django
from celery import Celery

# Define the default Django settings module for the 'celery' app.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# This will ensure that all the Django settings are loaded before Celery starts
# processing tasks. It is crucial for tasks that depend on Django models and other
# settings.
django.setup()

# Create an instance of the Celery class with a name of 'config'.
# https://docs.celeryq.dev/en/stable/reference/celery.html#celery.Celery
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
