import csv

with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    reader = [row for index, row in enumerate(reader)]
    reader = list(filter(lambda n: int(n[-1]) <= 1000, reader))
    reader = list(sorted(reader, key=lambda x: int(x[-1])))
    buys = [0]
    
    if reader:
        for i in reader:
            while buys[0] + int(i[-1]) <= 1000 and buys.count(i[0]) < 10:
                if buys[0] + int(i[-1]) <= 1000 and buys.count(i[0]) < 10:
                    buys[0] += int(i[-1])
                    buys.append(i[0])

    if len(reader) == 0:
        print('error')
    else:
        print(', '.join(buys[1:]))
