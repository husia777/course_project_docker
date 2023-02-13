from app.models import User


def test_login(client):
    user = User.objects.create(username='huseinnaimov@bk.ru', password=1606)
    
    response = client.get('/login/')

    assert response.status_code == 200
