import requests
from random import choice

base_url = "http://localhost:5585"
method = choice(["PATCH", "OPTIONS", "LOCK", "LINK"])


def test_not_found_endpoint():
    response = requests.request(method, url=base_url + "/device3")
    assert response.status_code == 404
