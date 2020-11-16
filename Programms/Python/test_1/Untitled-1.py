a = ['a', 'e', 'i', 'o', 'u']
b = [i.lower() for i in input().split('$')]
c = 0
d = 0
for i in b:
    for j in a:
        if j in i:
            c += 1
    if c == 1:
        d += 1
    c = 0
print(d)