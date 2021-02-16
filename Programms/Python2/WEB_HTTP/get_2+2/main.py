import requests
import json

server, port, a, b = input(), input(), input(), input()
params = {
    'a': a,
    'b': b
}

response = requests.get(f"{server}:{port}", params=params)
json_response = response.json()

print(' '.join(sorted(json_response["result"])))
print(json_response["check"])
