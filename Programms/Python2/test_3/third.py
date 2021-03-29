import argparse
import requests
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('host')
parser.add_argument('port')
parser.add_argument('param')
parser.add_argument('--accuracy', type=int, default=1)
parser.add_argument('--mult', type=int, default=1)

args = parser.parse_args()

response = requests.get(f"http://{args.host}:{args.port}")
json_response = response.json()

result = json_response[args.param]
data = []

for i in result:
    info = []
    sums = 0
    k = 0
    minus = []
    min_sas = []
    for j in i:
        if i[j] % args.mult == 0:
            sums += i[j]
            k += 1
            if int(i[j]) < 0:
                minus.append([i[j], j])
            if int(i[j]) > 100:
                min_sas.append([i[j], j])
    minus = sorted(minus)
    min_sas = sorted(min_sas)
    info.append(str(minus[0][-1]))
    info.append(str(minus[0][0]))
    info.append(str(min_sas[0][-1]))
    info.append(str(min_sas[0][0]))
    info.append(str(round(sums / k, args.accuracy)))
    data.append(info)


with open('location.csv', 'w', newline='') as f:
    writer = csv.writer(
        f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in data:
        writer.writerow(i)
