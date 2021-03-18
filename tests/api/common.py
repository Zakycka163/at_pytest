import requests


base_url = "http://localhost:5585"


def get_device_addresses():
    body = requests.get(base_url + "/devices").json()
    arr = []
    for i in range(0, len(body)):
        arr.append(body[i]["address"])
    return arr