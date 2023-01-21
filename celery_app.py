import os

from django.core.mail import EmailMessage
from app.services import list_emails_and_files
from config.settings import EMAIL_HOST_USER, BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# send_mail(
#     'Email Subject here',
#     'Email content',
#     EMAIL_HOST_USER,
#     ['huseinnaimov@bk.ru'])

msg = EmailMessage('Subject of the Email', 'Body of the email', EMAIL_HOST_USER, ['huseinnaimov@bk.ru'])
msg.content_subtype = "html"
print(list_emails_and_files)
msg.attach_file('/media/user_files/main.py')
msg.send()
