import json
import requests


with open('params.json') as json_file:
    data = json.load(json_file)
response = requests.get(f"http://{data['server']}:{data['port']}")
json_response = response.json()


experimental = json_response["experimental"]
calculated = json_response["calculated"]
module_sum = 0

for i in range(len(experimental)):
    module_sum += abs(experimental[i] - calculated[i])
res = module_sum / len(experimental)
print(round(res, 3))
