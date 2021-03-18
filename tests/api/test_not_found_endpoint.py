import requests

base_url = "http://localhost:5585"


def test_not_found_endpoint():
    response = requests.get(base_url + "/device3")
    assert response.status_code == 404
