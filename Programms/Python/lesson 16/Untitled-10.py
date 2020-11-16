a = []
for i in range(int(input())):
    c = [j for j in input().split(',')]
    a.append(c)
b = []
for i in range(int(input())):
    c = [j for j in input().split(',')]
    b.append(c)
for i in b:
    print(a[int(i[0])][int(i[-1])])