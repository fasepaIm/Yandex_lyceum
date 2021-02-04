import csv


def check():
    data = [[]]
    with open('alpha_oriona.csv', encoding='utf8') as results:
        results = csv.DictReader(results, delimiter=';')
        res = []
        for num, row in enumerate(results):
            if len(res) == 0:
                res.append(row)
            elif int(row['luminosity']) <= int(res[-1]['luminosity']):
                res.append(row)
            else:
                if len(res) > len(data[0]):
                    data[0] = res
                res = []
                res.append(row)

    if len(res) > len(data[0]):
        data[0] = res

    with open('result.txt', 'w', encoding='utf8') as end:
        end.write(f'{len(data[0])}\n')
        end.write(f"{data[0][0]['date']} {data[0][0]['time']}")


check()
