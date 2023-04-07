import json
import os
import sys
from fastapi.testclient import TestClient
from main import app

# sys.append.path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

client = TestClient(app)


def test_new_blog():
    response = client.post("/blog/create", json={"title": "my test", "body": "working well", "postDate": "2023-03-29 13:53:29.915000+00:00"})
    assert response.status_code == 200
    assert response.json()['title'] == "my test"


