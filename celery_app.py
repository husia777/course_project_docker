import os

from django.core.mail import EmailMessage
from app.services import list_emails_and_files
from config.settings import EMAIL_HOST_USER, BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
for i in range(len(list_emails_and_files)):
    msg = EmailMessage('Subject of the Email', 'Body of the email', EMAIL_HOST_USER, [list_emails_and_files[i][0]])
    msg.content_subtype = "html"
    msg.attach_file(list_emails_and_files[i][1])
    msg.send()
