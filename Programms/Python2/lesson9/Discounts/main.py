import csv

with open('wares.csv', newline='', encoding='utf8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        if int(row['Old price']) > int(row['New price']):
            print(row['Name'])
