import os
from django.core.mail import send_mail


# from celery import Celery
# from django.conf import settings
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service_settings')
#
# app = Celery('service')
# app.config_from_object('django.conf:settings')
# app.conf.broker_url = settings.CELERY_BROKER_URL
# app.autodiscover_tasks()


# @app.task()
def send_result(email, filename):
    send_mail(email, filename,
              'admin@example.com',
              ['admin@example.com'])


send_result('naimovsarif411@gmail.com', 'sdfsdfds')
