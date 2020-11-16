a = []
b = []
for i in range(int(input())):
    a.append(input())
for i in a:
    d = i.split()
    if 'встал' in i:
        if 'встала' in i:
            b.append(i[0:i.find('встала') - 1])
        else:
            b.append(i[0:i.find('встал') - 1])
    if d[0] == 'Привет,':
        b.insert(b.index(i[i.find(',') + 2:i.find('!')]) + 1,
                 i[i.find('!') + 2:i.find('будет') - 1])
    if 'хватит' in d:
        del b[b.index(i[:i.find('хватит') - 2])]
for i in b:
    print(i)