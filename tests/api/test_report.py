import pytest
import requests
from common import get_device_addresses, base_url


reports = [100, 200, 300, 400]


@pytest.mark.parametrize("rep_id", reports)
@pytest.mark.parametrize("address", get_device_addresses())
def test_get_all_reports(rep_id, address):
    response = requests.get(base_url + "/report?address=" + str(address) + "&repId=" + str(rep_id))
    assert response.status_code == 200
