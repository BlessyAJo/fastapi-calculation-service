import pytest


@pytest.mark.parametrize("a,b,op,expected", [
    (10, 5, "addition", 15),
    (10, 5, "subtraction", 5),
    (10, 5, "multiplication", 50),
    (10, 5, "division", 2),
])
def test_calculate_endpoint(client, a, b, op, expected):
    response = client.post("/calculate", json={
        "a": a,
        "b": b,
        "type": op
    })

    assert response.status_code == 200
    assert response.json()["result"] == expected


def test_invalid_type(client):
    response = client.post("/calculate", json={
        "a": 10,
        "b": 5,
        "type": "invalid"
    })

    assert response.status_code == 422 or response.status_code == 400