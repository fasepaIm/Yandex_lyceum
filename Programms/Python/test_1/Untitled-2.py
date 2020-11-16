c = []
a = int(input())
b = [int(i) for i in input().split()]
for i in b:
    if (i % a) % 2 != 0:
        if i not in c:
            c.append(i)
for i in c:
    print(i, end=' ')