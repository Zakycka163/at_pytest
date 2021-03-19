import pytest
from jsonschema import Draft3Validator
from common import get_devices


count_devices = 5
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


def test_status():
    assert get_devices().status_code == 200


def test_response_headers():
    assert get_devices().headers["Content-Type"] == "application/json"


def test_body_count_elements():
    body = get_devices().json()
    assert len(body) == count_devices


def test_body_validate_by_schema():
    body = get_devices().json()
    assert Draft3Validator(schema).is_valid(body)
