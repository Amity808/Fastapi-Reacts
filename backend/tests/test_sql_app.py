from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_class import Base
from main import app
from db.database import get_db



SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_new_blog():
    response = client.post("/blog/create", json={"title": "my test", "body": "working well", "postDate": "2023-03-29 13:53:29.915000+00:00"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['title'] == "my test"