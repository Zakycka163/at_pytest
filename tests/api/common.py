import requests

base_url = "http://localhost:5585"
freq_enum = [1, 2, 5, 10, 20, 50, 100, 200, 500]
duty_values = list(range(0, 101))
reports = [100, 200, 300, 400]


def get_devices():
    return requests.get(base_url + "/devices")


def get_device_addresses():
    body = requests.get(base_url + "/devices").json()
    arr = []
    for i in range(0, len(body)):
        arr.append(body[i]["address"])
    return arr


def found_device_by_address(address):
    for device in get_devices().json():
        if device['address'] == address:
            return device
    else:
        return False
