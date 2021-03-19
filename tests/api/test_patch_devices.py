from random import sample
import pytest
import requests
from common import get_device_addresses, base_url, found_device_by_address, freq_enum, duty_values

method = "PATCH"
count_runs_exp = 2


@pytest.mark.parametrize("pin_1_pwm_f", sample(freq_enum, count_runs_exp))
@pytest.mark.parametrize("pin_2_pwm_f", sample(freq_enum, count_runs_exp))
@pytest.mark.parametrize("pin_1_pwm_d", sample(duty_values, count_runs_exp))
@pytest.mark.parametrize("pin_2_pwm_d", sample(duty_values, count_runs_exp))
@pytest.mark.parametrize("address", sample(get_device_addresses(), count_runs_exp))
def test_update_all_scope_pwd(address, pin_1_pwm_f, pin_2_pwm_f, pin_1_pwm_d, pin_2_pwm_d):
    response = requests.request(method, url=base_url +
                                "/devices?address=" + address +
                                "&freq1=" + str(pin_1_pwm_f) +
                                "&duty1=" + str(pin_1_pwm_d) +
                                "&freq2=" + str(pin_2_pwm_f) +
                                "&duty2=" + str(pin_2_pwm_d))
    assert response.status_code == 200
    assert response.text == "OK"
    # check deployed result
    state_device = found_device_by_address(address)
    assert (state_device["pin_1_pwm_d"] == pin_1_pwm_d and
            state_device["pin_1_pwm_f"] == pin_1_pwm_f and
            state_device["pin_2_pwm_d"] == pin_2_pwm_d and
            state_device["pin_2_pwm_f"] == pin_2_pwm_f)


@pytest.mark.parametrize("freq_val", sample(freq_enum, count_runs_exp))
@pytest.mark.parametrize("freq_type", ["pin_1_pwm_f", "pin_2_pwm_f", ""])
@pytest.mark.parametrize("duty_val", sample(duty_values, count_runs_exp))
@pytest.mark.parametrize("duty_type", ["pin_1_pwm_d", "pin_2_pwm_d", ""])
@pytest.mark.parametrize("address", sample(get_device_addresses(), count_runs_exp))
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
        # check deployed result
        state_device = found_device_by_address(address)
        assert (state_device[freq_type] == freq_val and
                state_device[freq_type] == duty_val)
