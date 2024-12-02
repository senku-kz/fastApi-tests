from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_no_real_roots():
    response = client.post("/solve", json={"a": 1, "b": 0, "c": 1})
    assert response.status_code == 200
    assert response.json() == {"solution": "No real roots"}


def test_single_root():
    response = client.post("/solve", json={"a": 1, "b": -2, "c": 1})
    assert response.status_code == 200
    assert response.json() == {"solution": [1.0]}


def test_two_roots():
    response = client.post("/solve", json={"a": 1, "b": -3, "c": 2})
    assert response.status_code == 200
    assert response.json() == {"solution": [1.0, 2.0]}


def test_infinite_solutions():
    response = client.post("/solve", json={"a": 0, "b": 0, "c": 0})
    assert response.status_code == 200
    assert response.json() == {"solution": "Infinite solutions"}


def test_no_solution():
    response = client.post("/solve", json={"a": 0, "b": 0, "c": 1})
    assert response.status_code == 200
    assert response.json() == {"solution": "No solution"}
