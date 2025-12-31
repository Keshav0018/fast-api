#
# from ..main import app
# from ..routers.todos import get_current_user
# from ..routers.todos import  get_db
# from fastapi import status
# from ..models import Todos
# from .utilis import *
#
#
#
# app.dependency_overrides[get_db] = override_get_db
# app.dependency_overrides[get_current_user] = ovverride_get_current_user
#
#
#
# def test_real_one_authenticated(test_todo):
#
#     response = client.get('todos/todos/1')
#     print(response)
#     assert response.status_code == status.HTTP_200_OK
#     print("RESPONSE JSON:", response.json())
#     assert response.json() == {
#         'title':'Test',
#         'description':'Test',
#         'priority':5,
#         'complete':False,
#         'owner_id':1,'id':1,}
#
# def test_read_one_authenticated_not_found(test_todo):
#     response = client.get('todos/todos/999')
#     assert response.status_code == status.HTTP_404_NOT_FOUND
#     print("RESPONSE JSON:", response.json())
#     assert response.json() == {'detail': 'Todo not found'}
#
#
# def test_create_todo(test_todo):
#     request_data= {
#         'title':'Test',
#         'description':'Test',
#         'priority':5,
#         'complete':False,
#         'owner_id':1,
#         'id':2,
#     }
#     response = client.post('/todos/todos', json=request_data)
#     assert response.status_code == status.HTTP_201_CREATED
#     db = TestingSessionLocal()
#     model = db.query(Todos).filter(Todos.id==2).first()
#     assert model.title == request_data['title']
#     assert model.description == request_data['description']
#     assert model.priority == request_data['priority']
#     assert model.complete == request_data['complete']
#     assert model.owner_id == request_data['owner_id']
#     assert model.id == request_data['id']
#
# def test_update_todo(test_todo):
#     request_data= {
#         'title':'change the title',
#         'description':'change the description',
#         'priority':5,
#         'complete':False,
#
#     }
#
#     response = client.put('todos//todos/1', json=request_data)
#     assert response.status_code == status.HTTP_200_OK
#     db = TestingSessionLocal()
#     model = db.query(Todos).filter(Todos.id==1).first()
#     assert model.title == request_data['title']
#     assert model.description == request_data['description']
#
#
# def test_delete_todo(test_todo):
#     response = client.delete('todos/todos/1')
#     assert response.status_code == status.HTTP_204_NO_CONTENT
#     db = TestingSessionLocal()
#     model = db.query(Todos).filter(Todos.id==1).first()
#     assert model is None
#
# def test_delete_todo_not_found(test_todo):
#     response = client.delete('todos/todos/999')
#     assert response.status_code == 404
#
#
#

