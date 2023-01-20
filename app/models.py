from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'username'
    REQUIRED_FIELDS = []


class File(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_files/')
