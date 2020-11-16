words = []
vords = {}
lords = {}
x = set()
z = []
for i in range(int(input())):
    a = input().split()
    for j in a:
        if j[-1].isalpha():
            words.append(j.capitalize())
        else:
            words.append(j[:-1].capitalize())
for i in words:
    if i in vords:
        vords[i] += 1
    else:
        vords[i] = 1
for i in vords:
    if vords[i] in lords:
        lords[vords[i]] = lords[vords[i]] + ' ' + i
    if vords[i] not in lords:
        lords[vords[i]] = i
        x.add(vords[i])
for i in x:
    z.append(i)
z.sort(reverse=True)
for i in z:
    a = lords[i].split()
    a.sort()
    for j in a:
        print(j)