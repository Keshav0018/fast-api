from .utilis import *
from ..routers.admin import get_db,get_current_user
from ..models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = ovverride_get_current_user

def test_admin(test_todo):
    response = client.get(f'/admin/todos')
    assert response.status_code == status.HTTP_200_OK
    print(response.json())
    assert response.json() == [{'complete': False, 'id': 1, 'owner_id': 1, 'description': 'Test', 'priority': 5, 'title': 'Test'}]

def test_admin_delete(test_todo):
    response = client.delete(f'/admin/todos/{test_todo.id}')
    assert response.status_code == status.HTTP_204_NO_CONTENT
