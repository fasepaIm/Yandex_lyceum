import json
import requests


def basilisk(host, port, **kwargs):
    response = requests.get(f"http://{host}:{port}")
    json_response = response.json()
    for i in kwargs:
        if i in json_response:
            json_response[i].append(kwargs[i])
        else:
            json_response[i] = [kwargs[i]]
    return json_response
