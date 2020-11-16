a = input().lower()
b = list(a)
c = 0
for i in b:
    if a.count(i) > c:
        c = a.count(i)
print(c)