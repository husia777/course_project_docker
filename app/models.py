from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Choices


class User(AbstractUser):
    username = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'username'
    REQUIRED_FIELDS = []
    email_verify = models.BooleanField(default=False)

class File(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_files/')
    CHOICES = (
        ('Готов', 'COM'),  # Готов
        ('Ждет проверки', 'PEN'),  # В ожидании
        ('Проверяется', 'PER'),  # В исполнении
        ('Завершен с ошибкой', 'ER'),  # Ошибка
    )
    status = models.CharField(max_length=18, choices=CHOICES, default='Ждет проверки')
