from random import sample, choice
import pytest
import requests
from common import get_device_addresses, base_url


method = "PATCH"
not_allowed_method = choice(["PUT", "POST", "OPTIONS", "LOCK", "LINK"])
exp = 2


@pytest.mark.parametrize("freq_val", sample([-1, 3, 6, 11, 25, 57, 105, 501, "test"], exp))
@pytest.mark.parametrize("freq_type", ["freq1", "freq2", ""])
@pytest.mark.parametrize("duty_val", sample([-1, -100, 101, 200, 1000, "AT", "#"], exp))
@pytest.mark.parametrize("duty_type", ["duty1", "duty2", ""])
@pytest.mark.parametrize("address", sample(get_device_addresses(), exp))
def test_error_bad_request(address, freq_val, freq_type, duty_val, duty_type):
    duty = ""
    freq = ""
    if duty_type != "":
        duty = "&" + duty_type + "=" + str(duty_val)
    if freq_type != "":
        freq = "&" + freq_type + "=" + str(freq_val)
    response = requests.request(method, url=base_url + "/devices?address=" + address + duty + freq)
    assert response.status_code == 400, "Response text - " + response.text


def test_error_method_not_allowed():
    response = requests.request(not_allowed_method, url=base_url + "/devices")
    assert response.status_code == 405


@pytest.mark.parametrize("freq_val", [choice([1, 2, 5, 10, 20, 50, 100, 200, 500])])
@pytest.mark.parametrize("freq_type", [choice(["freq1", "freq2"])])
@pytest.mark.parametrize("duty_val", [choice(list(range(0, 101)))])
@pytest.mark.parametrize("duty_type", [choice(["duty1", "duty2"])])
@pytest.mark.parametrize("address", [choice([701, 777, "e213"])])
def test_error_not_found_device(address, freq_val, freq_type, duty_val, duty_type):
    duty = ""
    freq = ""
    if duty_type != "":
        duty = "&" + duty_type + "=" + str(duty_val)
    if freq_type != "":
        freq = "&" + freq_type + "=" + str(freq_val)
    response = requests.request(method, url=base_url + "/devices?address=" + address + duty + freq)
    assert response.status_code == 400, "Response text - " + response.text
