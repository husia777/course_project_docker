import os
# from time import sleep
#
from celery import shared_task
from django.core.mail import EmailMessage, send_mail
# from django.shortcuts import redirect
#
from app.services import list_emails_and_files
from config.settings import EMAIL_HOST_USER


#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


@shared_task
def send_all_result_to_mail(*args, **kwargs):
    for i in range(len(list_emails_and_files)):
        # send_mail('Subject of the Email', 'Body of 123 email', EMAIL_HOST_USER, [list_emails_and_files[i][0]])
        msg = EmailMessage('Subject of the Email', 'Body of 123 email', EMAIL_HOST_USER, [list_emails_and_files[i][0]])
        msg.content_subtype = "html"
        msg.attach(list_emails_and_files[i][1]) # полный путь
        msg.send()
        list_emails_and_files.clear()
    return
