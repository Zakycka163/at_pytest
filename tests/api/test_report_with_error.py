import pytest
import requests
from common import get_device_addresses, base_url
from random import sample, choice


invalid_reports = [101, -200, "300", 500]
reports = [100, 200, 300, 400]
not_allowed_method = choice(["PUT", "POST", "OPTIONS", "LOCK", "LINK"])


@pytest.mark.parametrize("params", ["?address=4A", "?repId=100"])
def test_error_bad_request(params):
    response = requests.get(base_url + "/report" + params)
    assert response.status_code == 400


@pytest.mark.parametrize("rep_id", reports)
@pytest.mark.parametrize("address", [choice([701, 777, "e213"])])
def test_error_not_found_device(rep_id, address):
    response = requests.get(base_url + "/report?address=" + str(address) + "&repId=" + str(rep_id))
    assert response.status_code == 404


@pytest.mark.parametrize("rep_id", [choice(invalid_reports)])
@pytest.mark.parametrize("address", sample(get_device_addresses(), 3))
def test_error_not_found_report(rep_id, address):
    response = requests.get(base_url + "/report?address=" + str(address) + "&repId=" + str(rep_id))
    assert response.status_code == 404


def test_error_method_not_allowed():
    response = requests.request(not_allowed_method, url=base_url + "/report")
    assert response.status_code == 405
