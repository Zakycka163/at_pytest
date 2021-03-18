import requests
from common import base_url


def test_not_found_endpoint():
    response = requests.get(base_url + "/device3")
    assert response.status_code == 404
