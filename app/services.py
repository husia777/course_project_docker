import os
from config.settings import BASE_DIR
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
operation_number = 0

list_emails_and_files = []


def check_and_write_result_to_file(filename, email, operation_num):
    path = os.path.join(BASE_DIR, "media")
    path = os.path.join(path, f"{filename}")
    path_to_result = os.path.join(BASE_DIR, "result")
    path_to_result = os.path.join(path_to_result, f"{operation_num}.txt")
    os.system(f" flake8 {path} > {path_to_result}")
    list_emails_and_files.append((email, path_to_result))


def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    context = {
        'user':user,
        'domain':current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user)
        }
    message = render_to_string('html/verify_email.html', context=context)
    email = EmailMessage('Verify email', message, to=[user.username],)
    email.send()