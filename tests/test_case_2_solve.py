import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_no_real_roots():
    response = client.post("/math/solve", json={"a": 1, "b": 0, "c": 1})
    assert response.status_code == 200
    assert response.json() == {"solution": "No real roots"}


def test_single_root():
    response = client.post("/math/solve", json={"a": 1, "b": -2, "c": 1})
    assert response.status_code == 200
    assert response.json() == {"solution": [1.0]}


def test_two_roots():
    response = client.post("/math/solve", json={"a": 1, "b": -3, "c": 2})
    assert response.status_code == 200
    assert response.json() == {"solution": [1.0, 2.0]}


def test_infinite_solutions():
    response = client.post("/math/solve", json={"a": 0, "b": 0, "c": 0})
    assert response.status_code == 200
    assert response.json() == {"solution": "Infinite solutions"}


def test_no_solution():
    response = client.post("/math/solve", json={"a": 0, "b": 0, "c": 1})
    assert response.status_code == 200
    assert response.json() == {"solution": "No solution"}


@pytest.mark.parametrize(
    "input_data, expected_status, expected_response",
    [
        # Test 6: Two roots
        (
            {"a": 1, "b": -3, "c": 2},
            200,
            {"solution": [1.0, 2.0]}
        ),
        # Test 7: One root (D=0)
        (
            {"a": 1, "b": -2, "c": 1},
            200,
            {"solution": [1.0]}
        ),
        # Test 8: No real roots
        (
            {"a": 1, "b": 1, "c": 1},
            200,
            {"solution": "No real roots"}
        ),
        # Test 9: Linear equation
        (
            {"a": 0, "b": 2, "c": -4},
            200,
            {"solution": [2.0]}
        ),
        # Test 10: Impossible equation
        (
            {"a": 0, "b": 0, "c": 1},
            200,
            {"solution": "No solution"}
        ),
        # Test 11: Infinite solutions
        (
            {"a": 0, "b": 0, "c": 0},
            200,
            {"solution": "Infinite solutions"}
        ),
    ],
)
def test_solve_quadratic(input_data, expected_status, expected_response):
    response = client.post("/math/solve", json=input_data)
    assert response.status_code == expected_status
    assert response.json() == expected_response
