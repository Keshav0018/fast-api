from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
from fastapi import status
import pytest
from ..models import Todos,User
from ..routers.auth import bcrypt_context




SQLALCHEMY_DATABASE_URI = "sqlite:///./testdb.db"

engine = create_engine(SQLALCHEMY_DATABASE_URI,
                       connect_args={"check_same_thread": False},
                       poolclass=StaticPool)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def ovverride_get_current_user():
    return {
        'username': 'Keshav',
        'id':1,
        'user_role':'admin'
    }

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title='Test',
        description='Test',
        priority=5,
        complete=False,
        owner_id=1,
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM todos'))
        connection.commit()

def test_real_all_authenticated(test_todo):

    response = client.get('/')
    print(response)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        'title':'Test',
        'description':'Test',
        'priority':5,
        'complete':False,
        'owner_id':1,'id':1,}]


@pytest.fixture
def test_user():
    user = User(
        username='Keshav',
        email='keshavchandak@gmail.com',
        first_name='Keshav',
        last_name='Chandak',
        hashed_password=bcrypt_context.hash("1234"),
        phone_number='+55 55 555',
        )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM users;'))
        connection.commit()
