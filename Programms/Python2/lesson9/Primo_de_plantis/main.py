import sys
import csv


data = list(map(str.strip, sys.stdin))
title = ('nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia')
for i in range(len(data)):
    data[i] = data[i].split('\t')

with open('plantis.csv', 'w', newline='') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(title)
    for i in data:
        writer.writerow(i)
