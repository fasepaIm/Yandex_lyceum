mens = []
a = 0
for i in range(int(input())):
    mens.append(input())
k = int(input())
m = int(input())
for i in range(m):
    for j in mens[::k]:
        if a != 0:
            del mens[a]
        a += (k - 1)
    a = 0
for i in mens:
    print(i)