import pytest
import requests
from jsonschema import Draft3Validator
from common import base_url


schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "address": {
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "pin_1_pwm_d": {
                "type": "number",
                "minimum": 0,
                "maximum": 100
            },
            "pin_1_pwm_f": {
                "type": "number",
                "enum": [1, 2, 5, 10, 20, 50, 100, 200, 500]
            },
            "pin_2_pwm_d": {
                "type": "number",
                "minimum": 0,
                "maximum": 100
            },
            "pin_2_pwm_f": {
                "type": "number",
                "enum": [1, 2, 5, 10, 20, 50, 100, 200, 500]
            },
            "type": {
                "type": "string",
                "enum": ["ECM", "PCM", "TCM", "BCM", "CCM"]
            },
        }
    }
}


def get_devices():
    return requests.get(base_url + "/devices")


def test_status():
    assert get_devices().status_code == 200


def test_response_headers():
    assert get_devices().headers["Content-Type"] == "application/json"


@pytest.mark.parametrize("count_devices", [5])
def test_body_count_elements(count_devices):
    body = get_devices().json()
    assert len(body) == count_devices


def test_body_validate_by_schema():
    body = get_devices().json()
    assert Draft3Validator(schema).is_valid(body)
