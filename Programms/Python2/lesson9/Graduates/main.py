import csv

people = {}
with open('vps.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index != 0:
            people[row[0]] = int(row[-2])


def check_graduates(percent):
    for i in people:
        if people[i] >= percent:
            print(i)


check_graduates(int(input()))
