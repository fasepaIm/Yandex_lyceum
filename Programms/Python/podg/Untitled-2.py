a = []
b = 'NO'
c = 0
for i in range(int(input())):
    a.append(int(input()))
for i in a[:-1]:
    for j in range(a.index(i) + 1, len(a) - 1):
        if i * a[j] % 6 == 0:
            print(i, a[j])
            c = 1
if c != 1:
    print(b)