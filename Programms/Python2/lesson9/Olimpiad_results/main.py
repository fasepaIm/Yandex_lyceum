import csv


def check(info):
    people = {}
    with open('rez.csv', encoding='utf8') as results:
        results = csv.DictReader(results, delimiter=',')
        for i in results:
            if list(map(int, i['login'].split('-')[2:4])) == info:
                if i['Score'] not in people:
                    people[i['Score']] = [i['user_name'].split()[-2]]
                else:
                    people[i['Score']] += [i['user_name'].split()[-2]]
    return people


pupa = check(list(map(int, input().split())))
for i in pupa:
    surnames = sorted(pupa[i], reverse=True)
    for surname in surnames:
        print(f'{surname} {i}')
