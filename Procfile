web: gunicorn config.wsgi
worker: celery -A config worker --loglevel=info
beat: celery -A config beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler