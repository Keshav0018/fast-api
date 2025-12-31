from .utilis import *
from ..routers.admin import get_db,get_current_user
from ..models import Todos
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = ovverride_get_current_user

def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == 200

# def test_change_password(test_user):
#     response = client.put('/user/change_password',json={ 'password': '1234',
#     'new_password': 'str'})
#     assert response.status_code == 200