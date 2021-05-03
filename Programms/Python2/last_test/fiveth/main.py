import argparse
import csv
import json

from flask import Flask

parser = argparse.ArgumentParser()
parser.add_argument("--address")
parser.add_argument("--port")
parser.add_argument("--filename")
args = parser.parse_args()
app = Flask(__name__)


@app.route('/manticore/')
def nuna():
    with open('hi.json', 'r') as cat_file:
        return json.load(cat_file)


def main():
    app.run(port=args.port, host=args.address)


with open(args.filename, encoding='UTF-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';', quotechar='"')
    bb = []
    rows = []
    for index, row in enumerate(reader):
        rows.append(row)
        for i in list(row.keys())[2:]:
            if row[i] not in bb:
                bb.append(row[i])
    dictonary = {}
    for i in bb:
        dictonary[i] = []
    for i in rows:
        if i['creature'] not in dictonary[i['head']]:
            dictonary[i['head']].append(i['creature'])
        if i['creature'] not in dictonary[i['body']]:
            dictonary[i['body']].append(i['creature'])
        if i['creature'] not in dictonary[i['tail']]:
            dictonary[i['tail']].append(i['creature'])
    for i in dictonary:
        dictonary[i] = sorted(dictonary[i])
with open('hi.json', 'w') as cat_file:
    json.dump(dictonary, cat_file)
main()
