import csv
import sys


results_data = []
data = list(map(str.strip, sys.stdin))
need = data[0].split()
for i in range(1, len(data)):
    test = data[i].split()
    if sum(list(map(int, test[2:]))) >= int(need[0]) and\
            len(list(filter(lambda n: int(n) >= int(need[1]), test[2:]))) == 3:
        results_data.append({
            'Фамилия': test[0],
            'имя': test[1],
            'результат 1': test[2],
            'результат 2': test[3],
            'результат 3': test[4], 
            'сумма': sum(list(map(int, test[2:]))),
        })

with open('exam.csv', 'w', newline='') as f:
    writer = csv.DictWriter(
        f, fieldnames=list(results_data[0].keys()), delimiter=';')
    writer.writeheader()
    for d in results_data:
        writer.writerow(d)
