import csv


words = set(['treasure', 'island', 'trove', 'map'])
dates = [int(i) for i in input().split()]
names = []
with open('mouth_shut.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in enumerate(reader):
        if row[-1][-1].isdigit():
            if int(row[-1][-1]) >= dates[0] and int(row[-1][-1]) <= dates[-1]:
                if set(row[-1][2].lower().split()) & words:
                    if row[-1][-1] not in names:
                        names.append(row[-1][1])
print('; '.join(sorted(names)))
