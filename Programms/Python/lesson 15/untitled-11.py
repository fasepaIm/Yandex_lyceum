a = input().lower()
b = list(a)
c = 0
d = ''
for i in b:
    if a.count(i) == c and i != ' ':
        if i < d:
            c = a.count(i)
            d = i
    else:
        if a.count(i) > c and i != ' ':
            c = a.count(i)
            d = i
print(d)