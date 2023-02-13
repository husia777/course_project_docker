import datetime
import pytest
import pytz
from django.test import TestCase

from app.models import User


@pytest.mark.django_db
def test_login(client):
	password = 1606
	username = '123@bk.ru'
	user = User.objects.create(username=username, password=password)
	now = datetime.datetime.today()
	now_utc = pytz.utc.localize(now)
	user = User.objects.get(username=username)
	user.set_password(password)

	expected_response = {
		'id': user.pk,
		'username': username,
		'last_login': None,
		'is_superuser': False,
		'first_name': None,
		'last_name': None,
		'email': username,
		'date_joined': now_utc,
		'is_active': True,
		'is_staff': False

	}

	response = client.post('/register/')

	assert response.status_code == 200
	assert response.data == expected_response
