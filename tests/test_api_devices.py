import requests


def test_status():
    response = requests.get("http://localhost:5585/devices")
    assert response.status_code == 200


def test_headers():
    response = requests.get("http://localhost:5585/devices")
    assert response.headers["Content-Type"] == "application/json"


def test_body_count_elements():
    response = requests.get("http://localhost:5585/devices")
    response_body = response.json()
    assert len(response_body) == 5
