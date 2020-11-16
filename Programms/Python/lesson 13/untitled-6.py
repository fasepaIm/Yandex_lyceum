a = []
b = []
for i in range(int(input())):
    a.append(input())
    b.append(input())
for i in range(len(a) - 1, -1, -1):
    print(a[i], b[i])