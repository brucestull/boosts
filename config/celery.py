from dotenv import load_dotenv
import os

import django
from celery import Celery

#######################################
from django.conf import settings as s

# print("s.EMAIL_HOST: ", s.EMAIL_HOST)
# print("s.ENVIRONMENT: ", s.ENVIRONMENT)
print("os.getenv('EMAIL_HOST'): ", os.getenv("EMAIL_HOST"))
print("os.getenv('ENVIRONMENT'): ", os.getenv("ENVIRONMENT"))
#######################################

load_dotenv()

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
