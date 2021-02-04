import csv


data = []


def check():
    with open('salary.csv', encoding='utf8') as results:
        results = csv.DictReader(results, delimiter=';')
        for i in results:
            if i['Федеральный округ'] == district:
                if int(i[start_year]) + int(i[start_year]) * 0.04 > int(i[end_year]):
                    data.append({
                        'Субъект': i['Субъект'],
                        start_year: i[start_year],
                        end_year: i[end_year]
                    })

    if data:
        with open('out_file.csv', 'w', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=list(data[0].keys()), delimiter=';')
            writer.writeheader()
            for d in data:
                writer.writerow(d)


district = input()
start_year, end_year = input().split()
check()
