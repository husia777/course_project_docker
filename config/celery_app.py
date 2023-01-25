import os

from celery import Celery
from config.settings import CELERY_BROKER_URL
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config', broker=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = CELERY_BROKER_URL
app.autodiscover_tasks()

# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html
