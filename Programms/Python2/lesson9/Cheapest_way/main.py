import csv


routes = []
routes_1 = []
routes_2 = []
results = {}
with open('input.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        routes.append(row)
    for i in routes[:-1]:
        if i[0] == routes[-1][0] and i[0:-1] != routes[-1][0:-1]:
            routes_1.append(i)
        if i[0:-1] == routes[-1][0:-1]:
            results[int(i[-1])] = ' '.join(i[0:-1])
        if i[1] == routes[-1][1]:
            routes_2.append(i)
    for i in routes_1:
        for j in routes_2:
            if i[1] == j[0]:
                results[int(i[-1]) + int(j[-1])] = ' '.join(i[:-1] + [j[1]])

cheapest_way = sorted(results)[0]
print(results[cheapest_way])
