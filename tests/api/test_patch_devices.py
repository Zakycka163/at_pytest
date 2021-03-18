from random import sample
import pytest
import requests

base_url = "http://localhost:5585"
method = "PATCH"
exp = 2


def get_device_addresses():
    body = requests.get(base_url + "/devices").json()
    arr = []
    for i in range(0, len(body)):
        arr.append(body[i]["address"])
    return arr


@pytest.mark.parametrize("freq1", sample([1, 2, 5, 10, 20, 50, 100, 200, 500], exp))
@pytest.mark.parametrize("freq2", sample([1, 2, 5, 10, 20, 50, 100, 200, 500], exp))
@pytest.mark.parametrize("duty1", sample(list(range(0, 101)), exp))
@pytest.mark.parametrize("duty2", sample(list(range(0, 101)), exp))
@pytest.mark.parametrize("address", sample(get_device_addresses(), exp))
def test_update_all_scope_pwd(address, freq1, freq2, duty1, duty2):
    response = requests.request(method, url=base_url +
                                "/devices?address=" + address +
                                "&freq1=" + str(freq1) +
                                "&duty1=" + str(duty1) +
                                "&freq2=" + str(freq2) +
                                "&duty2=" + str(duty2))
    assert response.status_code == 200
    assert response.text == "OK"


@pytest.mark.parametrize("freq_val", sample([1, 2, 5, 10, 20, 50, 100, 200, 500], exp))
@pytest.mark.parametrize("freq_type", ["freq1", "freq2", ""])
@pytest.mark.parametrize("duty_val", sample(list(range(0, 101)), exp))
@pytest.mark.parametrize("duty_type", ["duty1", "duty2", ""])
@pytest.mark.parametrize("address", sample(get_device_addresses(), exp))
def test_update_mixed_pwd(address, freq_val, freq_type, duty_val, duty_type):
    if duty_type == freq_type == "":
        pass
    else:
        duty = ""
        freq = ""
        if duty_type != "":
            duty = "&" + duty_type + "=" + str(duty_val)
        if freq_type != "":
            freq = "&" + freq_type + "=" + str(freq_val)
        response = requests.request(method, url=base_url + "/devices?address=" + address + duty + freq)
        assert response.status_code == 200, "Response has text - " + response.text
        assert response.text == "OK"
